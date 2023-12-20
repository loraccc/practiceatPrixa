from django.contrib import admin
from django.urls import path,include
from tryModel import views
from .views import *

urlpatterns = [
    # path('', views.index),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('upload', upload_file,name='upload'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    # path('success/', views.success, name='success'),
]


