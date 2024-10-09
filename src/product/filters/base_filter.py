from abc import ABC, abstractmethod


class ProductFilter(ABC):
    @abstractmethod
    def filter(self, queryset, search_query=None, category_id=None):
        pass
