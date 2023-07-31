
from django.urls import path
from .views import index, MenuView, BookingView
# Url Routes
urlpatterns = [
    path('', index, name='home'),
    path('menu/', MenuView.as_view(),name="menu"),
    path('booking/', BookingView.as_view(), name="booking"),
]
