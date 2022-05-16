from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def home(request):
    response = {'status' : 200 , 'message' : 'hi , from rest'}
    return response()
@api_view()
def mydetails(request):
    mydetail = {
        "name" :"amritpal singh",
        "age" : "23"

    }
  
    return Response({"payload": mydetail})

