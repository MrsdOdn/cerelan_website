from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from news_comment.models import NewsComment
from news_comment.serializers import NewsCommentSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.renderer import JSONResponseRenderer
from ceralan_website.core.permissions import IsOwner


class NewsCommentCreateList(generics.ListCreateAPIView):
    serializer_class = NewsCommentSerializer
    queryset = NewsComment.active.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ['author', 'news']
    search_fields = ['content']
    ordering_fields = '__all__'
    renderer_classes = [JSONResponseRenderer]


class NewsCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsCommentSerializer
    queryset = NewsComment.active.all()
    permission_classes = [permissions.IsAdminUser | IsOwner]
