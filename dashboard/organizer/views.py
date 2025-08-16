from rest_framework import generics, permissions
from .serializers import OrganizedEventsSerializer, CreateEventSerializer
# from .models import VolunteerSignup
from django.http import HttpResponse
import csv
from .models import volunteerroaster
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class OrganizedEventView(generics.ListAPIView):
    serializer_class = OrganizedEventsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'date', 'volunteer_name', 'role', 'location']
    filterset_fields = {'date': ['exact', 'contains'],
                        'location': ['exact', 'contains']
                        }

    def get_queryset(self):
        user = self.request.user
        return OrganizedEventView.objects.filter(organizer=user).select_related('organizer')
    

class CreateRetrieveUpdateDeleteEventView(generics.CreateAPIView):
    serializer_class = CreateEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


    def export_volunteer_roster(request):
        # Logic to export volunteer roster
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="volunteer_roster.csv"'

        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Location', 'Role', 'Phone Number', 'Address', 'Skills', 'Joined At'])

        for volunterroaster in volunterroaster.objects.all().values_list('full_name', 'location', 'role', 'phone_number', 'address', 'skills', 'joined_at'):
            writer.writerrow(volunteerroaster)


        return response