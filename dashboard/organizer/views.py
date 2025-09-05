from rest_framework import generics, permissions
from .serializers import CRUDEventSerializer, OrganizedEventListSerializer, OrganizedEventDetailSerializer, OngoingOrganizedListSerializer, OngoingOrganizedDetailSerializer, OngoingVolunteeredListSerializer, OngoingVolunteeredDetailSeriializer, VolunteeredListSerializer, VolunteeredDetailSeriallizer
from event.models import Event
# from .models import VolunteerSignup
from django.http import HttpResponse
import csv
from .models import volunteerroaster
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class  CRUDEventView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CRUDEventSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class OngoingOrganizedListView(generics.ListAPIView):
    serializer_class = OngoingOrganizedListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows current volunteer list for the event created by the logged in organizer
        event_id = self.kwargs['event_id']
        user = self.request.user
        return OngoingOrganizedListView.objects.filter(event__id=event_id, event__organizer=user).select_related('event', 'volunteer')
    
class OngoingOrganizedDetailView(generics.RetrieveAPIView):
    serializer_class = OngoingOrganizedDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of specific volunteer for the event ongoing
        event_id = self.kwargs['event_id']
        user = self.request.user
        return OngoingOrganizedDetailView.objects.filter(event__id=event_id, event__organizer=user).select_related('event', 'volunteer')
    
class OngoingVolunteeredListView(generics.ListAPIView):
    serializer_class = OngoingVolunteeredListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): # shows list of volunteers for ongoing events the user organized
        user = self.request.user
        return OngoingVolunteeredListView.objects.filter(event__organizer=user).select_related('event', 'volunteer')
    
class OngoingVolunteeredDetailView(generics.RetrieveAPIView):
    serializer_class = OngoingVolunteeredDetailSeriializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of a specific volunteer for ongoing events the user organized
        user = self.request.user
        return OngoingVolunteeredDetailView.objects.filter(event__organizer=user).select_related('event', 'volunteer')

class OrganizedEventListView(generics.ListAPIView):
    serializer_class = OrganizedEventListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'date', 'volunteer_name', 'role', 'location']

    def get_queryset(self): #shows events organized by the logged in organizer
        user = self.request.user
        return OrganizedEventListView.objects.filter(organizer=user).select_related('organizer')
    
    def export_volunteer_roster(request):
        # Logic to export volunteer roster
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="volunteer_roster.csv"'

        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Location', 'Role', 'Phone Number', 'Address', 'Skills', 'Joined At'])

        for volunterroaster in volunterroaster.objects.all().values_list('full_name', 'location', 'role', 'phone_number', 'address', 'skills', 'joined_at'):
            writer.writerrow(volunteerroaster)


        return response

class OrganizedEventDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = OrganizedEventDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self): #shows details of a specific event organized by the logged in organizer
        user = self.request.user
        return OrganizedEventDetailView.objects.filter(organizer=user).select_related('organizer')
    
class VolunteeredListView(generics.ListAPIView):
    serializer_class = VolunteeredListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows list of volunteers volunteered under the events created by the logged in organizer
        user = self.request.user
        return VolunteeredListView.objects.filter(event__organizer=user).select_related('event', 'volunteer')
    
class VolunteeredDetailView(generics.RetrieveAPIView):
    serializer_class = VolunteeredDetailSeriallizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of a specific volunteer volunteered under the events created by the logged in organizer
        user = self.request.user
        return VolunteeredDetailView.objects.filter(event__organizer=user).select_related('event', 'volunteer')