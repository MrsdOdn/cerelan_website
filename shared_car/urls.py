from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shared_car.views import SharedCarDetail, SharedCarCreateList

urlpatterns = [
                  path('', SharedCarCreateList.as_view()),
                  path('<int:pk>/', SharedCarDetail.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
