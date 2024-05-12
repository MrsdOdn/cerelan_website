from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from ceralan_website.core.permissions import IsOwnerOrReadOnly
from minibus.models import Minibus
from minibus.serializers import MinibusSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer


# Create your views here.


class MinibusCreateList(generics.ListCreateAPIView):
    serializer_class = MinibusSerializer
    queryset = Minibus.active.all()
    permission_classes = [  # yalnızca kimlik doğrulaması yapılmış kullanıcılara yazma izinleri sağlar.
        permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = (
        'pickup_location', 'drop_off_location', 'pickup_time', 'price', 'route', 'driver_first_name',
        'driver_last_name',)
    search_fields = (
        'pickup_location', 'drop_off_location', 'pickup_time', 'price', 'route', 'driver_first_name',
        'driver_last_name',)
    ordering_fields = ('created_at',)
    renderer_classes = [JSONResponseRenderer]


class MinibusDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MinibusSerializer
    queryset = Minibus.active.all()
    permission_classes = [IsOwnerOrReadOnly]
