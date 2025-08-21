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
    
    def clean(self):
        if self.status == self.Status.CONFIRMED:
            if self.event.is_full():
                raise ValidationError("This event has no available volunteer slots")
            existing_confirmed = VolunteerSignup.objects.filter(event=self.event,volunteer=self.volunteer,status=self.Status.CONFIRMED).exclude(id=self.id).exists()
            
            if existing_confirmed:
                raise ValidationError("Volunteer is already confirmed for this event")

    def save(self, *args, **kwargs):
        is_new = self._state.adding  # Check if this is a new object
        # Run validation
        self.full_clean()
        # Call original save
        super().save(*args, **kwargs)
        # Update volunteer count if status changed to/from CONFIRMED
        if is_new or 'status' in self.get_deferred_fields():
            self.update_volunteer_count()
            
    def update_volunteer_count(self):
        """Update the event's volunteer count based on confirmed signups"""
        confirmed_count = VolunteerSignup.objects.filter(
            event=self.event,
            status=self.Status.CONFIRMED
        ).count()
        
        # Update the event's current_volunteers field
        Event.objects.filter(id=self.event.id).update(
            current_volunteers=confirmed_count
        )

    def delete(self, *args, **kwargs):
        """Handle volunteer count when signup is deleted"""
        event_id = self.event.id
        super().delete(*args, **kwargs)
        # Update count after deletion
        confirmed_count = VolunteerSignup.objects.filter(
            event_id=event_id,
            status=self.Status.CONFIRMED
        ).count()
        
        Event.objects.filter(id=event_id).update(
            current_volunteers=confirmed_count
        )
