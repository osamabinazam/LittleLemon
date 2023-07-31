from rest_framework import serializers
from .models  import Menu, Booking

# Creating Serializers


# Menu Serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# Booking Serializer
class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'