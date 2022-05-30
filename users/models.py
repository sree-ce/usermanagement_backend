from django.db import models
from django.contrib.auth .models import AbstractUser
# Create your models here.


class UserRegistration(AbstractUser):

    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username
