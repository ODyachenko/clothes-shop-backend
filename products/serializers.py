from rest_framework import serializers
from .models import Category, Product, Review, ProductSize, ProductImage, Cart, ProductColor, Brand
from users.serializers import ReviewAuthorSerializer
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = ['id', 'name', 'logo']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'value']

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['id', 'value']


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField(required=False)
    rating = serializers.SerializerMethodField(read_only=True)
    images = ProductImageSerializer(many=True, required=False)
    sizes = ProductSizeSerializer(many=True)
    colors = ProductColorSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    dress_style = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'description', 'details', 'category', 'dress_style', 'discount', 'price', 'inventory', 'images', 'sizes', 'colors', 'on_sale', 'rating', 'reviews', 'create_at']

    def get_category(self, obj):
        return obj.category.name

    def get_brand(self, obj):
        return obj.brand.name if obj.brand else ''

    def get_dress_style(self, obj):
        return obj.dress_style.name

    def get_discount(self, obj):
        return obj.discount.value if obj.discount else 0

    def get_details(self, obj):
        return obj.details.split('\r\n') if obj.details else []

    def get_rating(self, obj):
        reviews = Review.objects.filter(product=obj)
        return sum(review.rating for review in reviews) / reviews.count() if reviews.exists() else 0

    def get_reviews(self, obj):
        from .serializers import ReviewSerializer
        reviews = Review.objects.filter(product=obj)
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

   
    def create(self, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')
        validated_data.pop('images', None)  # Remove images from validated_data
        product = Product.objects.create(**validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)
        return product

    def update(self, instance, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')
        instance = super().update(instance, validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=instance, image=image_data)
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    user = ReviewAuthorSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'text', 'create_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    productItemId = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='productItem'
    )
    productItem = ProductSerializer(read_only=True)

    def create(self, validated_data):
        product_item_id = validated_data.pop('productItem').id  # Get the ID of the product item
        product_item = Product.objects.get(pk=product_item_id)

        cart_item = Cart.objects.create(
            productItem=product_item,
            **validated_data
        )
        return cart_item

    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'color', 'size', 'unit_price', 'total_price', 'productItem', 'productItemId', 'user', 'create_at']

        extra_kwargs = {
            'total_price': {'read_only': True}
        }
