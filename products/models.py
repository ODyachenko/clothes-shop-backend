from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    value = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.value


class ProductSize(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='media/products_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)
    size = models.ForeignKey(ProductSize, on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.color} | {self.size} | {self.inventory} units'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products_images')

class Review(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} | {self.product.color} | {self.rating} stars'