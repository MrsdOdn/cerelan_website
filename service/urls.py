from django.urls import path

from service.views import ServiceDetail, ServiceCreateList

urlpatterns = [
    path('', ServiceCreateList.as_view()),
    path('<int:pk>/', ServiceDetail.as_view()),
]
