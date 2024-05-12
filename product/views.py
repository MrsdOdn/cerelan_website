from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from ceralan_website.core.permissions import IsOwnerOrReadOnly
from product.models import Product
from product.serializers import ProductSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer


# Create your views here.


class ProductCreateList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.active.all()
    permission_classes = [  # yalnızca kimlik doğrulaması yapılmış kullanıcılara yazma izinleri sağlar.
        permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = (
        'parent_category__name', 'subcategory__name', 'seller_first_name', 'seller_last_name', 'delivery_option')
    search_fields = (
        'parent_category__name', 'subcategory__name', 'seller_first_name', 'seller_last_name', 'delivery_option')
    ordering_fields = ('created_at',)
    renderer_classes = [JSONResponseRenderer]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.active.all()
    permission_classes = [IsOwnerOrReadOnly]
