from django.shortcuts import render

#  Imports Related to REST API Development
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking,Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.


# Home View that reder index.html page to the browser
def index (request):
    context = {}
    return render(request, 'index.html', context)


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