from rest_framework import serializers
from .models import User, Event, VolunteerSignup

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'role', 'bio']
        extra_kwargs = {
            'password': {'write_only': True},
            'name': {'source': 'get_full_name', 'read_only': True}
        }

class EventSerializer(serializers.ModelSerializer):
    organizers = UserSerializer(many=True, read_only=True)
    available_slots = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'organizers', 'available_slots']

class VolunteerSignupSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    volunteer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role=User.Role.VOLUNTEER),
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = VolunteerSignup
        fields = ['id', 'event', 'volunteer', 'status', 'signed_up_at', 'notes']
        read_only_fields = ['status', 'signed_up_at']
    
    def validate(self, data):
        if data['volunteer'].role != User.Role.VOLUNTEER:
            raise serializers.ValidationError("Only volunteers can sign up for events.")
        return data