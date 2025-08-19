from django.urls import path
from .views import OrganizedEventView, CRUDEventView

urlpatterns = [
    path('organizedevents/', OrganizedEventView.as_view(), name='organized_events'),
    path('organizeevents/', CRUDEventView.as_view(), name='create_event'),
    # path()
]