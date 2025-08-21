from django.db import models
from django.core.exceptions import ValidationError
from users.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    max_volunteers = models.PositiveIntegerField(default=10, help_text="Maximum number of volunteers allowed")
    current_volunteers = models.PositiveIntegerField(default=1, help_text="Current number of volunteers")
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.max_volunteers > 60: 
            raise ValidationError("Maximum volunteers cannot exceed 60")
        if self.max_volunteers < 1:
            raise ValidationError("Must allow at least 1 volunteer")

    def is_full(self):
        return self.current_volunteers >= self.max_volunteers 

    def available_slots(self):
        return self.max_volunteers - self.current_volunteers()

    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation
        super().save(*args, **kwargs)