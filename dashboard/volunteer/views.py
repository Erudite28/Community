# from django.shortcuts import render
from .serializers import VolunteerDashboardSerializer, volunteeredDsahboardSerializer
from rest_framework import generics, permissions
from volunteersignup.models import VolunteerSignup
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class VolunteerDashboardView(generics.ListAPIView):
    serializer_class = VolunteerDashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self , serializer):
        user = self.request.user
        return serializer.save(volunteer_name=user.username)

class VolunteeredDashboardView(generics.ListAPIView):
    serializer_class = volunteeredDsahboardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'date', 'location']
    

    def get_queryset(self):
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username)