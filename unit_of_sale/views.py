from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from unit_of_sale.models import UnitOfSale
from unit_of_sale.serializers import UnitOfSaleSerializer


# Create your views here.
class UnitOfSaleCreateList(generics.ListCreateAPIView):
    serializer_class = UnitOfSaleSerializer
    queryset = UnitOfSale.active.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       MyOrderingFilter]
    filterset_fields = 'unit_name'
    search_fields = 'unit_name'
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class UnitOfSaleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UnitOfSaleSerializer
    queryset = UnitOfSale.active.all()
