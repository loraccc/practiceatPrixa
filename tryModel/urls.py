from django.contrib import admin
from django.urls import path,include
from tryModel import views
from .views import upload_file

urlpatterns = [
    # path('', views.index),
    path('upload', upload_file,name='upload'),
     path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]


