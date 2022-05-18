import email
from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length= 50) 
    email1 = models.CharField(max_length = 50)
    bio = models.CharField(max_length=50)

    def __str__(self):
        return self.name

        