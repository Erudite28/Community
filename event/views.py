from rest_framework import generics,permission
from .models import User,Event
from serializers import UserSerializer,EventSerializer
from rest_framework.permissions import BasePermission

class IsOrganizer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user

# Create your views here.
