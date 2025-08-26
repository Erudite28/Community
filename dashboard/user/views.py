from .serializers import EventsListSerializer, EventDetailSerializer
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class EventsListView(generics.ListAPIView):
  serializer_class = EventsListSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
 #  filterset_fields = {'title': ['exact', 'contains'],
 #                     'location': ['exact', 'contains']
 #                     }
  search_fields = ['title', 'locations']

  def get_queryset(self): #shows all events
   return EventsListView.objects.all().select_related('organizer')

class EventDetailView(generics.RetrieveDestroyAPIView):
   serializer_class = EventDetailSerializer
   permission_classes = [permissions.IsAuthenticated]

   def get_queryset(self): #shows details of a specific event
      return EventDetailView.objects.all().select_related('organizer')
