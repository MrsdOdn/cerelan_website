from django.urls import path
from bus_stop.views import BusStopDetail, BusStopCreateList

urlpatterns = [
    path('', BusStopCreateList.as_view()),
    path('<int:pk>/', BusStopDetail.as_view()),
]
