from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from ceralan_website.core.permissions import IsOwnerOrReadOnly
from shared_car.models import SharedCar
from shared_car.serializers import SharedCarSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer


# Create your views here.


class SharedCarCreateList(generics.ListCreateAPIView):
    serializer_class = SharedCarSerializer
    queryset = SharedCar.active.all()
    permission_classes = [  # yalnızca kimlik doğrulaması yapılmış kullanıcılara yazma izinleri sağlar.
        permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = (
        'pickup_location', 'drop_off_location', 'pickup_time', 'price', 'route', 'driver_first_name',
        'driver_last_name', 'number_of_passengers')
    search_fields = (
        'pickup_location', 'drop_off_location', 'pickup_time', 'price', 'route', 'driver_first_name',
        'driver_last_name', 'number_of_passengers')
    ordering_fields = ('created_at',)
    renderer_classes = [JSONResponseRenderer]


class SharedCarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SharedCarSerializer
    queryset = SharedCar.active.all()
    permission_classes = [IsOwnerOrReadOnly]
