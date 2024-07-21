from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from car_image.models import CarImage
from car_image.serializers import CarImageSerializer


# Create your views here.
class CarImageCreateList(generics.ListCreateAPIView):
    serializer_class = CarImageSerializer
    queryset = CarImage.active.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ['id', 'created_at', ]
    search_fields = ['id', 'created_at']
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class CarImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarImageSerializer
    queryset = CarImage.active.all()
