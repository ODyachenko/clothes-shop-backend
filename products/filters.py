import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'price', 'colors', 'sizes', 'on_sale']

class CustomProductFilter(ProductFilter):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ProductFilter.Meta.fields + ['min_price', 'max_price']