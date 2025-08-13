from django.urls import path
from .views import (EventListView,EventCreateView,EventRetrieveUpdateDestroyView)
 
urlpatterns = [
    path('event/', EventListView.as_view(), name='event-list'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
]
