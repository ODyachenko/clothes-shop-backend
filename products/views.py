from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Category, Product, Review, Cart, ProductColor, Brand
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CartSerializer, ProductColorSerializer, BrandSerializer
from .paginations import ProductsPaginations
from .filters import CustomProductFilter

# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BrandsView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ColorsView(generics.ListAPIView):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ProductsPaginations
    filterset_class = CustomProductFilter

    ordering_fields = ['price', 'rating', 'create_at']
    search_fields = ['title']


class SingleProductView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewsView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    ordering_fields = ['rating', 'create_at']
    filterset_fields = ['rating']

class SingleReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartItemsView(generics.ListCreateAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Cart.objects.all().filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        Cart.objects.all().filter(user=self.request.user).delete()
        return Response({'Message':'Your items have been deleted.'}, status.HTTP_200_OK)

class SingleCartItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

