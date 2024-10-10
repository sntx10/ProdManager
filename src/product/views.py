from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .services.product_service import ProductService
from .filters.postgres_filter import PostgresProductFilter


@method_decorator(cache_page(60 * 1), name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_service = ProductService(PostgresProductFilter())

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('created_at')
        search_query = self.request.GET.get('q', None)
        category_id = self.request.GET.get('category', None)

        return self.product_service.get_products(queryset, search_query, category_id)


@method_decorator(cache_page(60 * 1), name='dispatch')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

