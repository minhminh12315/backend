import django_filters
from .models import Variant

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='product__category__name',lookup_expr='icontains')

    class Meta:
        model = Variant
        fields = ['category']