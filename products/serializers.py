from rest_framework import serializers
from .models import Category, Product, Review, ProductSize, ProductImage
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)
    # images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'description', 'price', 'size', 'color', 'inventory', 'rating']

    def get_rating(self, obj):
        reviews = Review.objects.filter(product=obj)
        return sum(review.rating for review in reviews) / reviews.count() if reviews.exists() else 0
    
    # def create(self, validated_data):
    #     images_data = self.context.get('request').FILES.getlist('images') 
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, image=image_data)
    #     return product
            

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'text', 'create_at']