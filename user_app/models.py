from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('VOLUNTEER', 'volunteer'),
        ('ORGANIZER', 'organizer'),
    ]
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='VOLUNTEER')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self

# Create your models here
    