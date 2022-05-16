from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index),
    path('show_fruits', views.show_fruits,name = "show fruits"),
    path('delete_fruits/<id>', views.delete_fruit, name = 'delete_fruits'),
    path('dynamic/<slug>', views.dynamic , name='dynamic'),
    path('login', views.login_page, name='login'),
    path('register',views.register_page, name='register')


    
]