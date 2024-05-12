from django.urls import path

from car_image.views import CarImageDetail, CarImageCreateList

urlpatterns = [
    path('', CarImageCreateList.as_view()),
    path('<int:pk>/', CarImageDetail.as_view()),
]
