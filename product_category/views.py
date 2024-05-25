from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from product_category.models import ProductCategory
from product_category.serializers import ProductCategorySerializer


# Create your views here.
class ProductCategoryCreateList(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.active.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       MyOrderingFilter]
    filterset_fields = ['name', 'parent__name']
    search_fields = ['name', 'parent__name']
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.active.all()
    permission_classes = [permissions.IsAuthenticated]
