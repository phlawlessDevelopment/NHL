from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NHLUser(AbstractUser):
    '''Model for users'''
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)