from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

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
    image = models.ImageField(upload_to='products_images', null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    inventory = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)
    size = models.ForeignKey(ProductSize, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    create_at = models.DateField(auto_now_add=True)