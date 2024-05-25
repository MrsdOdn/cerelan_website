from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from service.models import Service
from service.serializers import ServiceSerializer


# Create your views here.
class ServiceCreateList(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.active.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       MyOrderingFilter]
    filterset_fields = 'city'
    search_fields = 'city'
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.active.all()
    permission_classes = [permissions.IsAuthenticated]
