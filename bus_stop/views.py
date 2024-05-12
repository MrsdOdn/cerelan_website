from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from bus_stop.models import BusStop
from bus_stop.serializers import BusStopSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer


# Create your views here.
class BusStopCreateList(generics.ListCreateAPIView):
    serializer_class = BusStopSerializer
    queryset = BusStop.active.all()
    permission_classes = [permissions.IsAdminUser]  # Herkese görünmesine izin verir, sadece adminler oluşturabilir
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ('service__city', 'stop_name', 'price', 'departure_time', 'return_time')
    search_fields = ('service__city', 'stop_name', 'price', 'departure_time', 'return_time')
    ordering_fields = ('created_at',)  # Sadece 'created_at' alanı için sıralama yapılabilir
    renderer_classes = [JSONResponseRenderer]


class BusStopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BusStopSerializer
    queryset = BusStop.active.all()
    permission_classes = [permissions.IsAuthenticated]
