from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from news_image.models import NewsImage
from news_image.serializers import NewsImageSerializer


# Create your views here.
class NewsImageCreateList(generics.ListCreateAPIView):
    serializer_class = NewsImageSerializer
    queryset = NewsImage.active.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ['news__title']  # filter images based on the associated news
    search_fields = ['news__title']  # search images based on the title of the associated news
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class NewsImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsImageSerializer
    queryset = NewsImage.active.all()
