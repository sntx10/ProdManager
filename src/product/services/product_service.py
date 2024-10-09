from ..filters.base_filter import ProductFilter


class ProductService:
    def __init__(self, product_filter: ProductFilter):
        self.product_filter = product_filter

    def get_products(self, queryset, search_query=None, category_id=None):
        return self.product_filter.filter(queryset, search_query, category_id)
