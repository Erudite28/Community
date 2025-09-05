from django.urls import path
from .views import CRUDEventView, OrganizedEventListView, OrganizedEventDetailView, OngoingOrganizedListView, OngoingOrganizedDetailView, OngoingVolunteeredListView, OngoingVolunteeredDetailView, VolunteeredListView, VolunteeredDetailView

urlpatterns = [
    path('organizeevents/', CRUDEventView.as_view(), name='create_event'),
    path('organizedeventslist/', OrganizedEventListView.as_view(), name='organized-events-list'),
    path('organizedeventsdetail/<int:pk>/', OrganizedEventDetailView.as_view(), name='organized-event-detail'),
    path('ongoingvolunteeredlist/<int:event_id>/', OngoingOrganizedListView.as_view(), name='current-volunteered-list'),
    path('ongoingvolunteereddetail/<int:pk>/', OngoingOrganizedDetailView.as_view(), name='current-volunteered-detail'),
    path('ongoingvolunteeredlist/', OngoingVolunteeredListView.as_view(), name='ongoing-volunteered-list'),
    path('ongoingvolunteereddetail/<int:pk>/', OngoingVolunteeredDetailView.as_view(), name='ongoing-volunteered-detail'),
    path('volunteeredlist/', VolunteeredListView.as_view(), name='volunteered-list'),
    path('volunteereddetail/<int:pk>/', VolunteeredDetailView.as_view(), name='volunteered-detail'),
#    path('exportroster/', CRUDEventView.export_volunteer_roster, name='export-roster'),
]