# from django.shortcuts import render
from .serializers import VolunteerDashboardSerializer, VolunteeredDetailSerializer, VolunteeredListSerializer, OngoingVolunteeredEventListSeriaalizer, OngoingVolunteeredEventDetailSerializer, UpcomingVolunteeredListSerializer, UpcomingVolunteeredDetailSerializer
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
    
class OngoingVolunteeredEventListView(generics.ListAPIView):
    serializer_class = OngoingVolunteeredEventListSeriaalizer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'title', 'date', 'location']

    def get_queryset(self): #shows ongoing events volunteered by the logged in volunteer
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username, status='ongoing').select_related('event')
    
class OngoingVolunteeredEventDetailView(generics.RetrieveAPIView):
    serializer_class = OngoingVolunteeredEventDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of a specific ongoing event volunteered by the logged in volunteer
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username, status='ongoing').select_related('event')
    
class UpcomingVolunteeredListView(generics.ListAPIView):
    serializer_class = UpcomingVolunteeredListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'title', 'date', 'location']

    def get_queryset(self): #shows upcoming events volunteered by the logged in volunteer
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username, status='upcoming').select_related('event')
    
class UpcomingVolunteeredDetailView(generics.RetrieveAPIView):
    serializer_class = UpcomingVolunteeredDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #shows details of a specific upcoming event volunteered by the logged in volunteer
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username, status='upcoming').select_related('event')


class VolunteeredListView(generics.ListAPIView):
    serializer_class = VolunteeredListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'date', 'location']
    

    def get_queryset(self):
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username)
    
class VolunteeredDetailView(generics.RetrieveAPIView):
    serializer_class = VolunteeredDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #returns the info of the logged in volunteer
        user = self.request.user
        return VolunteerSignup.objects.filter(volunteer_name=user.username)
    