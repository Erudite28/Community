from rest_framework import serializers
from event.models import Event
#from .serializers import  EventSerializer
from volunteersignup.models import VolunteerSignup

class CRUDEventSerializer(serializers.ModelSerializer):
   # events to be created by organizers
   class Meta:
      model = Event
      fields = ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'phone_number']
      read_only_fields = ['id']

   def create(self, validated_data):
      validated_data['organizer'] = self.context['request'].user
      return super().create(**validated_data)
   
   def update(self, instance, validated_data):
      instance.title = validated_data.get('title', instance.title)
      instance.description = validated_data.get('description', instance.description)
      instance.date = validated_data.get('date', instance.date)
      instance.location = validated_data.get('location', instance.location)
      instance.max_volunteers = validated_data.get('max_volunteers', instance.max_volunteers)
      instance.phone_number = validated_data.get('phone_number', instance.phone_number)
      instance.save()
      return instance   

# class OrganizedEventsSerializer(serializers.ModelSerializer):
#   #  events organized by the organizers
#    class Meta:
#       model= Event, VolunteerSignup
#       fields = ['id', 'location', 'title', 'volunteer_name', 'volunteer_phone_number', 'role', 'status', 'date']
#       read_only_fields = ['id', 'location', 'title', 'volunteer_name', 'volunteer_phone_number', 'role', 'status', 'date']

class CurrentVolunteeredListSerializer(serializers.ModelSerializer): #to show current volunteer list for the event creaated
   class Meta:
      model = VolunteerSignup
      fields = ['id', 'volunteer_name']
      read_only_fields = ['id']

      
   def get_volunteer_count(self, obj):
    return obj.volunteersignup_set.count()

class CurrentVolunteeredDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = VolunteerSignup
      fields = ['id', 'volunteer_name', 'volunteer_phone_number', 'role', 'status']
      read_only_fields = ['id', 'volunteer_name', 'volunteer_phone_number', 'role', 'status']


class OrganizedEventListSerializer(serializers.ModelSerializer):
   class Meta:
      model = Event
      fields = ['id', 'title']
      read_only_fields = ['id', 'title']
    
   def get_volunteer_count(self, obj):
    return obj.volunteersignup_set.count()


class OrganizedEventDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = Event
      fields = ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'phone_number', 'volunteer_count']
      read_only_fields = ['id', 'title', 'description', 'date', 'location', 'max_volunteers', 'phone_number', 'volunteer_count']