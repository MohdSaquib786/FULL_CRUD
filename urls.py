
from django.contrib import admin
from django.urls import path
from onetooneapp import views

urlpatterns = [
    path('index/', views.index),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('profileupdate/<str:pk>/',views.profile_update,name='profile_update'),
    path('profiledelete/<str:pk>/', views.profile_delete, name='profile_delete'),

]
