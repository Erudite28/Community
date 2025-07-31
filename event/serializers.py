from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizers = UserSerializer(many=True, read_only=True)
    available_slots = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'organizers', 'available_slots']
