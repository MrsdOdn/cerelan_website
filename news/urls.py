from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from news.views import NewsDetail, NewsCreateList

urlpatterns = [
                  path('', NewsCreateList.as_view()),
                  path('<int:pk>/', NewsDetail.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
