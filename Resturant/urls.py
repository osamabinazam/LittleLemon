
from django.urls import path
from .views import index, MenuView, BookingView, MenuItemsView, SingleMenuItemView
# Url Routes
urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
]
