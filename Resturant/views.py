from django.shortcuts import render

#  Imports Related to REST API Development
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking,Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# Home View that reder index.html page to the browser
def index (request):
    context = {}
    return render(request, 'index.html', context)


# Part of Video

#  This View Return a json respone that contains Booking Items
class BookingView (APIView):
    #  This method is called when a GET request is made to the view
    def get(self, requset):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data) 

class MenuView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data": serializer.data})
        


# Part of Exercises

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # return Response(serializer_class.data) 
    def get (self, request):
        return Response ({"data": request.data})    

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # return Response(serializer.da) 
    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    