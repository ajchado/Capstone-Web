from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=20)
    shortbio = models.CharField(max_length=100)
    isLoggedIn = models.BooleanField(default = False)


    
class Admin(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=20)
    shortbio = models.CharField(max_length=100)
    isLoggedIn = models.BooleanField(default = False)