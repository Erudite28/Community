from rest_framework import serializers
from .models import VolunteerSignup
from users.models import User
from event.models import Event
from event.serializers import EventSerializer

class VolunteerSignupSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    volunteer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role=User.Role.VOLUNTEER),default=serializers.CurrentUserDefault())
    event_details = EventSerializer(source='event', read_only=True)
    
    class Meta:
        model = VolunteerSignup
        fields = ['id', 'event', 'volunteer', 'status', 'signed_up_at', 'event_details']
        read_only_fields = ['volunteer', 'signed_up_at']

    def validate(self, data):
        """Custom validation for volunteer signups"""
        event = data.get('event') or self.instance.event if self.instance else None
        
        if event and event.is_full():
            raise serializers.ValidationError(
                f"This event is full. {event.available_slots()} slots available."
            )
        
        # Check for existing signup
        user = self.context['request'].user
        existing_signup = VolunteerSignup.objects.filter(event=event,volunteer=user,status__in=[VolunteerSignup.Status.PENDING, VolunteerSignup.Status.CONFIRMED]).exists()
        
        if existing_signup and (not self.instance or self.instance.volunteer != user):
            raise serializers.ValidationError("You have already signed up for this event")
        
        return data

    def create(self, validated_data):
        """Create signup with automatic volunteer assignment"""
        validated_data['volunteer'] = self.context['request'].user
        return super().create(validated_data)