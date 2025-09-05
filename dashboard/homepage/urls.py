from django.urls import path
from .views import EventsListView, EventDetailView

urlpatterns = [
    path('eventslist/', EventsListView.as_view(), name='events-list'),
    path('eventsdetail/<int:pk>/', EventDetailView.as_view(), name='events-detail')
]