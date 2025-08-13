from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import VolunteerSignup,User
from .serializers import VolunteerSignupSerializer

class VolunteerSignupListCreateView(generics.ListCreateAPIView):
    serializer_class = VolunteerSignupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return signups for the current user if they're a volunteer
        if self.request.user.role == User.Role.VOLUNTEER:
            return VolunteerSignup.objects.filter(volunteer=self.request.user)
        # Return all signups for organizers/admins
        return VolunteerSignup.objects.all()

    def perform_create(self, serializer):
        # Automatically set the volunteer to the current user
        serializer.save(volunteer=self.request.user)

class VolunteerSignupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerSignup.objects.all()
    serializer_class = VolunteerSignupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()

class EventVolunteersListView(generics.ListAPIView):
    serializer_class = VolunteerSignupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return VolunteerSignup.objects.filter(event_id=event_id)

class UpdateSignupStatusView(generics.UpdateAPIView):
    queryset = VolunteerSignup.objects.all()
    serializer_class = VolunteerSignupSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['patch']  # Only allow PATCH

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(VolunteerSignup.Status.choices):
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        instance.status = new_status
        instance.save()
        return Response(VolunteerSignupSerializer(instance).data)