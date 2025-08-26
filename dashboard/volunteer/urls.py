from django.urls import path
from .views import VolunteerDashboardView, VolunteeredListView, VolunteeredDetailView

urlpatterns = [
    path('volunteerdashboard/', VolunteerDashboardView.as_view(), name= 'volunteer-dashboard'),
    path('volunteeredlistdashboard/', VolunteeredListView.as_view(), name='volunteered-dashboard'),
    path('volunteereddetaildashboard/<int:pk>/', VolunteeredDetailView.as_view(), name='volunteered-detail-dashboard'),
]