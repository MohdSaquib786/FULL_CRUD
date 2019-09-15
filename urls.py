
from django.contrib import admin
from django.urls import path
from onetooneapp import views

urlpatterns = [
    path('index/', views.index),
    path('createprofile/', views.createprofile,name='createprofile'),

    #path('newprofile/', views.newprofile),

]
