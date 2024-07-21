from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.permissions import IsAdminOrReadOnly
from ceralan_website.core.renderer import JSONResponseRenderer
from delivery_option.models import DeliveryOption
from delivery_option.serializers import DeliveryOptionSerializer


# Create your views here.
class DeliveryOptionCreateList(generics.ListCreateAPIView):
    serializer_class = DeliveryOptionSerializer
    queryset = DeliveryOption.active.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       MyOrderingFilter]
    filterset_fields = ['option_name']
    search_fields = ['option_name']
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class DeliveryOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryOptionSerializer
    queryset = DeliveryOption.active.all()
    permission_classes = [permissions.IsAuthenticated]
