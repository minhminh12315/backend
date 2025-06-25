from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Remove username and email requirements
    username = None
    email = None
    
    # Custom fields
    fullname = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Use phone_number as the unique identifier
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  # Remove email from required fields
    
    def __str__(self):
        return self.phone_number
