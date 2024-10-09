from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F, Q
from .base_filter import ProductFilter


class PostgresProductFilter(ProductFilter):
    def filter(self, queryset, search_query=None, category_id=None):
        if search_query:
            search_query = ' '.join(search_query.split())
            query = SearchQuery(search_query)
            queryset = queryset.annotate(
                rank=SearchRank(F('search_vector'), query)
            ).filter(Q(rank__gte=0.03))

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset
