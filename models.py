from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user=models.CharField(max_length=64)
    designation=models.CharField(max_length=64)
    country=models.CharField(max_length=64)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id',]
