
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Resturant.views import BookingViewSet


# Registering Router
router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('Resturant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
