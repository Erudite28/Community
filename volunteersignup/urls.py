from django.urls import path
from .views import (VolunteerSignupListCreateView,VolunteerSignupRetrieveUpdateDestroyView,EventVolunteersListView,UpdateSignupStatusView)

urlpatterns = [
    path('signup/', VolunteerSignupListCreateView.as_view(), name='volunteer-signup-list'),
    path('signup/<int:pk>/', VolunteerSignupRetrieveUpdateDestroyView.as_view(),name='volunteer-signup-detail'),
    path('events/<int:event_id>/volunteers/', EventVolunteersListView.as_view(),name='event-volunteers-list'),
    path('signup/<int:pk>/status/', UpdateSignupStatusView.as_view(),name='update-signup-status'),
]