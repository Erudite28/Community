from django.urls import path
from .views import VolunteerDashboardView, VolunteeredDashboardView

urlpatterns = [
    path('volunteer/dashboard/', VolunteerDashboardView.as_view(), name= 'volunteer_dashboard'),
    path('volunteered/dashboard/', VolunteeredDashboardView.as_view(), name='volunteered_dashboard'),
]