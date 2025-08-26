from rest_framework import generics, permissions
from .serializers import CRUDEventSerializer, OrganizedEventListSerializer, OrganizedEventDetailSerializer, CurrentVolunteeredListSerializer, CurrentVolunteeredDetailSerializer
# from .models import VolunteerSignup
from django.http import HttpResponse
import csv
from .models import volunteerroaster
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class OrganizedEventView(generics.ListAPIView):
#     serializer_class = OrganizedEventsSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filterset_fields = {'date': ['exact', 'contains'],
#                         'location': ['exact', 'contains']
#                         }


    

class  CRUDEventView(generics.CreateAPIView):
    serializer_class = CRUDEventSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


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
    
class CurrentVolunteeredListView(generics.ListAPIView):
    serializer_class = CurrentVolunteeredListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows current volunteer list for the event created by the logged in organizer
        event_id = self.kwargs['event_id']
        user = self.request.user
        return CurrentVolunteeredListView.objects.filter(event__id=event_id, event__organizer=user).select_related('event', 'volunteer')
    
class CurrentVolunteeredDetailView(generics.RetrieveAPIView):
    serializer_class = CurrentVolunteeredDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of specific volunteer for the event ongoing
        event_id = self.kwargs['event_id']
        user = self.request.user
        return CurrentVolunteeredDetailView.objects.filter(event__id=event_id, event__organizer=user).select_related('event', 'volunteer')
    