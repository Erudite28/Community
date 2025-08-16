from django.urls import path
from .views import OrganizedEventView, CreateRetrieveUpdateDeleteEventView

urlpatterns = [
    path('organizedevents/', OrganizedEventView.as_view(), name='organized_events'),
    path('organizeevents/', CreateRetrieveUpdateDeleteEventView.as_view(), name='create_event'),
    # path()
]