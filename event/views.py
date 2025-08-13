from rest_framework import generics,permissions
from .models import User,Event
from .serializers import EventSerializer
from rest_framework.permissions import BasePermission

'''class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_object(self):
        if self.request.user.is_staff:  # Admins can access any user
            return super().get_object()
        return self.request.user  # Regular users can only access their own profile'''

# Event Views
class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Public read, auth required for write

    def get_queryset(self):
        queryset = Event.objects.all()
        
        # Filter by organizer if organizer_id is provided
        organizer_id = self.request.query_params.get('organizer_id')
        if organizer_id:
            queryset = queryset.filter(organizer__id=organizer_id)
            
        # Filter by volunteer if volunteer_id is provided
        volunteer_id = self.request.query_params.get('volunteer_id')
        if volunteer_id:
            queryset = queryset.filter(volunteers__id=volunteer_id)
            
        return queryset.order_by('-date')

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOrganizer()]
        return super().get_permissions()

class IsOrganizer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user