from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from news_category.models import NewsCategory
from news_category.serializers import NewsCategorySerializer


# Create your views here.
class NewsCategoryCreateList(generics.ListCreateAPIView):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.active.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       MyOrderingFilter]
    filterset_fields = 'name'
    search_fields = 'name'
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class NewsCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.active.all()
