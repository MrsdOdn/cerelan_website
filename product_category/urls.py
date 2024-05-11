from django.urls import path

from product_category.views import ProductCategoryDetail, ProductCategoryCreateList

urlpatterns = [
    path('', ProductCategoryCreateList.as_view()),
    path('<int:pk>/', ProductCategoryDetail.as_view()),
]
