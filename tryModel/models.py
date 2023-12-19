from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

class people(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
  