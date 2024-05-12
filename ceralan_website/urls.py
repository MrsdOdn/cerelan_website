"""
URL configuration for ceralan_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Project System API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# ViewSets define the view behavior.

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/account/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/account/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    re_path(r'^api/v1/users/', include('account.urls')),
    re_path(r'^api/v1/news_categories/', include('news_category.urls')),
    re_path(r'^api/v1/news/', include('news.urls')),
    re_path(r'^api/v1/news_images/', include('news_image.urls')),
    re_path(r'^api/v1/news_comments/', include('news_comment.urls')),
    re_path(r'^api/v1/units_of_sale/', include('unit_of_sale.urls')),
    re_path(r'^api/v1/delivery_options/', include('delivery_option.urls')),
    re_path(r'^api/v1/product_categories/', include('product_category.urls')),
    re_path(r'^api/v1/products/', include('product.urls')),
    re_path(r'^api/v1/product_images/', include('product_image.urls')),
    re_path(r'^api/v1/shared_cars/', include('shared_car.urls')),
    re_path(r'^api/v1/minibuses/', include('minibus.urls')),
    re_path(r'^api/v1/car_images/', include('car_image.urls')),
    re_path(r'^api/v1/services/', include('service.urls')),
    re_path(r'^api/v1/drivers/', include('driver.urls')),
    re_path(r'^api/v1/bus_stops/', include('bus_stop.urls')),
]
