from django.urls import path
from .views import VolunteerDashboardView, VolunteeredListView, VolunteeredDetailView, OngoingVolunteeredEventListView, OngoingVolunteeredEventDetailView, UpcomingVolunteeredListView, UpcomingVolunteeredDetailView

urlpatterns = [
    path('volunteerdashboard/', VolunteerDashboardView.as_view(), name= 'volunteer-dashboard'),
    path('volunteeredlistdashboard/', VolunteeredListView.as_view(), name='volunteered-dashboard'),
    path('volunteereddetaildashboard/<int:pk>/', VolunteeredDetailView.as_view(), name='volunteered-detail-dashboard'),
    path('ongoingvolunteeredlistdashboard/', OngoingVolunteeredEventListView.as_view(), name='ongoing-volunteered-list-dashboard'),
    path('ongoingvolunteereddetaildashboard/<int:pk>/', OngoingVolunteeredEventDetailView.as_view(), name='ongoing-volunteered-detail-dashboard'),
    path('upcomingvolunteeredlistdashboard/', UpcomingVolunteeredListView.as_view(), name='upcoming-volunteered-list-dashboard'),
    path('upcomingvolunteereddetaildashboard/<int:pk>/', UpcomingVolunteeredDetailView.as_view(), name='upcoming-volunteered-detail-dashboard'),
]