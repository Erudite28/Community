from django.urls import path
from .views import CRUDEventView, OrganizedEventListView, OrganizedEventDetailView, CurrentVolunteeredListView, CurrentVolunteeredDetailView

urlpatterns = [
#    path('organizedevents/', OrganizedEventView.as_view(), name='organized_events'),
    path('organizeevents/', CRUDEventView.as_view(), name='create_event'),
    path('organizedeventslist/', OrganizedEventListView.as_view(), name='organized-events-list'),
    path('organizedeventsdetail/<int:pk>/', OrganizedEventDetailView.as_view(), name='organized-event-detail'),
    path('currentvolunteeredlist/<int:event_id>/', CurrentVolunteeredListView.as_view(), name='current-volunteered-list'),
    path('currentvolunteereddetail/<int:pk>/', CurrentVolunteeredDetailView.as_view(), name='current-volunteered-detail'),
#    path('exportroster/', CRUDEventView.export_volunteer_roster, name='export-roster'),
]