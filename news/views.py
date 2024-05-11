from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from news.models import News
from news.serializers import NewsSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer


# Create your views here.
class NewsCreateList(generics.ListCreateAPIView):
    """
    Haberlerin listesini alır veya yeni bir haber oluşturur.

    Filtreleme Alanları:
        - `title`: Başlık alanına göre filtreleme yapar.
        - `news_category`: Haber kategorisine göre filtreleme yapar.

    Arama Alanları:
        - `title`: Başlık alanında arama yapar.
        - `news_category`: Haber kategorisinde arama yapar.

    Sıralama Alanları:
        - Sadece belirli alanlar için sıralama yapılabilir.
    """
    serializer_class = NewsSerializer
    queryset = News.active.all()
    permission_classes = [permissions.IsAdminUser]  # Herkese görünmesine izin verir, sadece adminler oluşturabilir
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ('title', 'news_category')
    search_fields = ('title', 'news_category')
    ordering_fields = ('created_at',)  # Sadece 'created_at' alanı için sıralama yapılabilir
    renderer_classes = [JSONResponseRenderer]


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.active.all()
    permission_classes = [permissions.IsAuthenticated]
