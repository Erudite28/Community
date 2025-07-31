from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    max_volunteers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def available_slots(self):
        return self.max_volunteers - self.volunteers.count()

