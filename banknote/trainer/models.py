from django.db import models
from django.urls import reverse

# Create your models here.
class Trainer(models.Model):
    Name=models.CharField(max_length=255)
    Title=models.CharField(max_length=255)
    Facebook_URL = models.URLField()
    Instagram_URL = models.URLField()
    Whatsapp_Number = models.CharField(max_length=255)
    Linkedin_URL = models.URLField()
    Image_URL = models.URLField()
    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("trainer:success")
