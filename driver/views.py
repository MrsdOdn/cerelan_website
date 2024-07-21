from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from ceralan_website.core.permissions import IsOwnerOrReadOnly
from driver.models import Driver
from driver.serializers import DriverSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from service.serializers import ServiceSerializer


# Create your views here.


class DriverCreateList(generics.ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.active.all()
    permission_classes = [  # yalnızca kimlik doğrulaması yapılmış kullanıcılara yazma izinleri sağlar.
        permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ('first_name', 'last_name', 'departure_location__city', 'address')
    search_fields = ('first_name', 'last_name', 'departure_location__city', 'address')
    ordering_fields = ('created_at',)
    renderer_classes = [JSONResponseRenderer]


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.active.all()
    permission_classes = [IsOwnerOrReadOnly]
