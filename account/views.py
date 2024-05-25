from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from account.models import MyUser
from account.permissions import AllowCreateListAdminOnly  # Özel izin sınıfını buraya ekledik
from account.serializers import UserSerializer
from ceralan_website.core.filter import MyOrderingFilter
from ceralan_website.core.permissions import IsOwner
from ceralan_website.core.renderer import (JSONResponseRenderer, JSONResponseRendererDetail)


# Create your views here.
class UserCreateList(generics.ListCreateAPIView):
    permission_classes = [AllowCreateListAdminOnly]  # Özel izin sınıfını burada kullanıyoruz
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, MyOrderingFilter]
    filterset_fields = ['email']  # Filterset fields should be a list or tuple
    search_fields = ['email', 'first_name', 'last_name']
    renderer_classes = [JSONResponseRenderer]
    ordering_fields = '__all__'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | IsOwner]  # Ensure proper permission usage
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    renderer_classes = [JSONResponseRendererDetail]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']  # Optional: Include search fields here if needed
