from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    Role=models.CharField(max_length=255,default="user")
    phone_number=models.CharField(max_length=255)
    Academic_Year=models.CharField(max_length=255)
    College=models.CharField(max_length=255)
    University=models.CharField(max_length=255)

    def __str__(self):
        return self.username
    class Meta:
        ordering = ["date_joined"]
