from datetime import datetime
import imp
from multiprocessing import context
import re
from django.shortcuts import render,redirect
from .models import *
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    if request.method == 'POST':
        fruit_name  = request.POST.get('fruit_name')
        price = request.POST.get('price')
        fruits_description = request.POST.get('fruits_description')

        Fruits.objects.create(
            fruit_name = fruit_name,
            price = price,

            fruits_description = fruits_description,
            manfacture_date = date.today()
        )
    return render(request , "home.html")

def show_fruits(request):
    context = {'fruits'  : Fruits.objects.all()}
    return render(request, "show_fruits.html",context)

def delete_fruit(request ,id):
    try: 
        fruits = Fruits.objects.get(id = id).delete()
    

    except Exception as e:
        print(e)

    return redirect('/')

def dynamic(request, slug):
    print(slug)
    return render(request, 'dynamic.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            return redirect('register.html')
        
        user_obj = authenticate(username = username, password = password)
        if user_obj:
            login(request,user_obj)
            return redirect('/show_fruits')

    return render(request, 'login.html')
            


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
    
        if User.objects.filter(username = username).exists():
            return redirect('register')
    
        user_obj = User.objects.create(
        username = username,
        first_name = first_name)
        user_obj.set_password(password)
        user_obj.save()

    return render(request, 'register.html')
    

    




    


