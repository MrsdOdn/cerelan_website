from django.urls import path

from unit_of_sale.views import UnitOfSaleDetail, UnitOfSaleCreateList

urlpatterns = [
    path('', UnitOfSaleCreateList.as_view()),
    path('<int:pk>/', UnitOfSaleDetail.as_view()),
]
