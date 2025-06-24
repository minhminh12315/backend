from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
