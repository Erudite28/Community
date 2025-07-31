from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser):
    class Role(models.TextChoices):
        VOLUNTEER = 'VOLUNTEER', 'volunteer'
        ORGANIZER = 'ORGANIZER', 'organizer'
        
    role = models.CharField(max_length=12, choices=Role.choices, default=Role.VOLUNTEER)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",  
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set", 
        related_query_name="user",
    )
