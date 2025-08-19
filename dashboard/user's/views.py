from .serializers import EventsListSerializer, EventDetailSerializer
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class EventsListView(generics.ListAPIView):
  serializer_class = EventDetailSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = {'title': ['exact', 'contains'],
                      'location': ['exact', 'contains']
                      }
  search_fields = ['title', 'locations']

  def get_querryset(self):
        user = self.request.user
        return EventsListView.objects.filter(user=user).select_related('organizer')