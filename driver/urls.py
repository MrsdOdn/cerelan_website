from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from driver.views import DriverDetail, DriverCreateList

urlpatterns = [
                  path('', DriverCreateList.as_view()),
                  path('<int:pk>/', DriverDetail.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
