from django.urls import path

from news_comment.views import NewsCommentDetail, NewsCommentCreateList

urlpatterns = [
    path('', NewsCommentCreateList.as_view()),
    path('<int:pk>/', NewsCommentDetail.as_view()),
]
