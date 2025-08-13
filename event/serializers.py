from rest_framework import serializers
from .models import User, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role']
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
