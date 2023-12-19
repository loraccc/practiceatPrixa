from django.contrib import admin
from django.urls import path,include
from tryModel import views

urlpatterns = [
    path('', views.index),
]
