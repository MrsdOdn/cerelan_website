from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from minibus.views import MinibusDetail, MinibusCreateList

urlpatterns = [
                  path('', MinibusCreateList.as_view()),
                  path('<int:pk>/', MinibusDetail.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
