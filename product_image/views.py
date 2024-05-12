from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from product_image.models import ProductImage
from product_image.serializers import ProductImageSerializer


# Create your views here.
class ProductImageCreateList(generics.ListCreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.active.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ['product__id', 'product__subcategory',
                        'product__parent_category']  # filter images based on the associated news
    search_fields = ['product__id', 'product__subcategory',
                     'product__parent_category']  # search images based on the title of the associated news
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.active.all()
