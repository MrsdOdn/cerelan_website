from django.urls import path

from news_category.views import NewsCategoryDetail, NewsCategoryCreateList

urlpatterns = [
    path('', NewsCategoryCreateList.as_view()),
    path('<int:pk>/', NewsCategoryDetail.as_view()),
]
