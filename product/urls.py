from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from product.views import ProductDetail, ProductCreateList

urlpatterns = [
                  path('', ProductCreateList.as_view()),
                  path('<int:pk>/', ProductDetail.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
