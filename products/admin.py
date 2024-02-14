from django.contrib import admin
from .models import Category, Product, ProductSize, ProductColor, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(Review)