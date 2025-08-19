from event.models import Event
from rest_framework import serializers

class EventsListSerializer(serializers.ModelSerializer):
  # user dashboard (shows events available for volunteering)
  class Meta :
    models = Event,
    fields = ['id', 'title', 'location']
    read_only_fields = ['id', 'title', 'location']

class EventDetailSerializer(serializers.ModelSerializer):
  # user dashboard (shows details of the event)
  class Meta:
    model = Event
    fields = '__all__'
    read_only_fields = '__all__'
    # ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'organizer', 'created_at', 'updated_at']

