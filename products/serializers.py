from rest_framework import serializers
from .models import Category, Product, Review, ProductSize, ProductImage, Cart, ProductColor
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

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
    rating = serializers.SerializerMethodField(read_only=True)
    images = ProductImageSerializer(many=True, required=False)
    sizes = ProductSizeSerializer(many=True)
    colors = ProductColorSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'details', 'category','discount', 'price', 'inventory', 'images', 'sizes', 'colors', 'on_sale', 'rating', 'reviews', 'create_at']

    def get_category(self, obj):
        return obj.category.name

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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'text', 'create_at']
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
    #     return super().create(validated_data)


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    
    def validate(self, attrs):
        attrs['total_price'] = attrs['quantity'] * attrs['unit_price']
        return attrs
    
    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'unit_price', 'total_price', 'productItem', 'user', 'create_at']

        extra_kwargs = {
            'total_price': {'read_only': True}
        }
