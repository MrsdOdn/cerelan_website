from django.urls import path

from delivery_option.views import DeliveryOptionDetail, DeliveryOptionCreateList

urlpatterns = [
    path('', DeliveryOptionCreateList.as_view()),
    path('<int:pk>/', DeliveryOptionDetail.as_view()),
]
