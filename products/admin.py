from django.contrib import admin
from .models import Category, DressStyle, Brand, Product, ProductSize, ProductColor, Review, ProductImage, Discount, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(DressStyle)
admin.site.register(Brand)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(Review)
admin.site.register(ProductImage)
admin.site.register(Cart)