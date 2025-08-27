from event.models import Event
from rest_framework import serializers
from volunteersignup.models import VolunteerSignup

class VolunteerDashboardSerializer(serializers.ModelSerializer):
#  (events available for volunteering)
  class Meta:         
    model = VolunteerSignup
    fields = ['__all__' ]
    read_only_fields = ['__all__']

class OngoingVolunteeredEventListSeriaalizer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'title', 'location', 'date']
    read_only_fields = ['id', 'title', 'location', 'date']

class OngoingVolunteeredEventDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'title', 'description', 'date', 'location', 'phone_number']
    read_only_fields = ['id', 'title', 'description', 'date', 'location', 'phone_nummber']

class UpcomingVolunteeredListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'title', 'location', 'date']
    read_only_fields = ['id', 'title', 'location', 'date']

class UpcomingVolunteeredDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'title', 'description', 'date', 'location', 'joined_at', 'role', 'status']
    read_only_fields = ['id', 'title', 'description', 'date', 'location', 'joined_at', 'role', 'status']


class VolunteeredListSerializer(serializers.ModelSerializer): #shows volunteered events list
  class Meta:
    model = Event
    fields = ['id', 'title', 'location', 'date']
    raed_only_fields = ['id', 'title', 'location', 'date']

class VolunteeredDetailSerializer(serializers.ModelSerializer): #shows details of a specific volunteered event
  class Meta:
    model = Event
    fields = ['id', 'title', 'description', 'date', 'location', 'joined_at', 'role', 'status']
    read_only_fields = ['id', 'title', 'description', 'date', 'location', 'joined_at', 'role', 'status']


# class volunteeredDsahboardSerializer(serializers.ModelSerializer):
#   event = VolunteerDashboardSerializer(read_only=True)
#   event_title = serializers.CharField(source='event.title', read_only=True)
#   event_date = serializers.DateField(source='event.date', read_only=True)
#               # (signed up events)
#   class Meta:
#     model = Event
#     fields = ['id', 'title', 'location', 'crated_at', 'end_time', 'date']
#     read_only_fields = ['id', 'title', 'location', 'created_at', 'end_time', 'date']