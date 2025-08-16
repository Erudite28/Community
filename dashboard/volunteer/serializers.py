from event.models import Event
from rest_framework import serializers

class VolunteerDashboardSerializer(serializers.ModelSerializer):
#  (events available for volunteering)
  class Meta:         
    model = Event
    fields = ['id', 'full_name', 'location', 'phone_number', 'address', 'skill', 'joined_at' ]
    read_only_fields = ['id', 'joined_date']

class volunteeredDsahboardSerializer(serializers.ModelSerializer):
  event = VolunteerDashboardSerializer(read_only=True)
  event_title = serializers.CharField(source='event.title', read_only=True)
  event_date = serializers.DateField(source='event.date', read_only=True)
              # (signed up events)
  class Meta:
    model = Event
    fields = ['id', 'title', 'location', 'crated_at', 'end_time', 'date']
    read_only_fields = ['id', 'title', 'location', 'created_at', 'end_time', 'date']