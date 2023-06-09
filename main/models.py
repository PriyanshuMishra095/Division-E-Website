from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    prn = models.IntegerField()
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    about = models.CharField(max_length=300)
    age = models.CharField(max_length=30)
    
class Login(models.Model):
    curr_user = models.CharField(max_length=30)