from django.urls import path
from .views import (RegisterAPI,LoginAPI,LogoutAPI,UserProfileAPI,OrganizerOnlyAPI,VolunteerOnlyAPI,UserListAPI)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('profile/', UserProfileAPI.as_view(), name='profile'),
    path('organizer/', OrganizerOnlyAPI.as_view(), name='organizer'),
    path('volunteer/', volunteerOnlyAPI.as_view(), name='volunteer'),
    path('user/', UserListAPI.as_view(), name='user-list'),
]