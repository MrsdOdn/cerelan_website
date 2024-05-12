from django.urls import path

from product_image.views import ProductImageDetail, ProductImageCreateList

urlpatterns = [
    path('', ProductImageCreateList.as_view()),
    path('<int:pk>/', ProductImageDetail.as_view()),
]
