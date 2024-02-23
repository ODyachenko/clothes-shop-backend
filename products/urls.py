from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('categories/<int:pk>', views.SingleCategoryView.as_view()),
    path('products', views.ProductsView.as_view()),
    path('products/<int:pk>', views.SingleProductView.as_view()),
    path('reviews', views.ReviewsView.as_view()),
    path('cart', views.CartItemsView.as_view()),
    path('cart/<int:pk>', views.SingleCartItemView.as_view()),
]
