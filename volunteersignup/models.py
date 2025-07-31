from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from event.models import Event

class VolunteerSignup(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='volunteers')
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signed_up_event')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    signed_up_at = models.DateTimeField(auto_now_add=True)