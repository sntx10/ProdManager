from rest_framework import viewsets
from rest_framework import permissions

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .services.product_service import ProductService
from .filters.postgres_filter import PostgresProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_service = ProductService(PostgresProductFilter())

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', None)
        category_id = self.request.GET.get('category', None)

        return self.product_service.get_products(queryset, search_query, category_id)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

