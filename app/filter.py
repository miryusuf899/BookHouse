import django_filters
from .models import Book

class FilterBook(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Book
        fields = ['title', 'price__gt', 'price__lt']