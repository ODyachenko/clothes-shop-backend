from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DressStyle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands_images', null=True)

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class ProductSize(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Discount(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.value}%'


class Product(models.Model):
    name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=400)
    details = models.TextField(max_length=1500, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)
    inventory = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    dress_style = models.ForeignKey(DressStyle, on_delete=models.PROTECT, default=1)
    colors = models.ManyToManyField(ProductColor, related_name='colors_list')
    sizes = models.ManyToManyField(ProductSize, related_name='sizes_list')
    on_sale = models.BooleanField(default=False, null=True)
    rating = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.inventory} units'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f'Image for {self.product.name}'


class Review(models.Model):
    rating = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} | {self.rating} stars'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productItem = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('productItem', 'user')
        ordering = ['-create_at']

    def __str__(self):
        return f"Cart item - {self.productItem.name}"
