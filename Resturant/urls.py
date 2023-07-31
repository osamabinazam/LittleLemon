
from django.urls import path
from .views import index
# Url Routes
urlpatterns = [
    path('', index, name='home'),
]
