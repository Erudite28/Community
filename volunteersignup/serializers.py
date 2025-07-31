from rest_framework import serializers
from .models import VolunteerSignup
from user.model import User
from event.model import Event

class VolunteerSignupSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    volunteer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role=User.Role.VOLUNTEER),
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = VolunteerSignup
        fields = ['id', 'event', 'volunteer', 'status', 'signed_up_at', 'notes']
        read_only_fields = ['id', 'status', 'signed_up_at']
    
    def validate(self, data):
        if data['volunteer'].role != User.Role.VOLUNTEER:
            raise serializers.ValidationError("Only volunteers can sign up for events.")
        return data