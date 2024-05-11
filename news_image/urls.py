from django.urls import path

from news_image.views import NewsImageDetail, NewsImageCreateList

urlpatterns = [
    path('', NewsImageCreateList.as_view()),
    path('<int:pk>/', NewsImageDetail.as_view()),
]
