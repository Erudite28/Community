from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import(CustomTokenObtainPairView,TokenRefreshView,RegisterView,CurrentUserView,LoginView,LogoutView,OrganizerOnlyView,VolunteerOnlyView)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', CurrentUserView.as_view(), name='current-user'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('organizer/', OrganizerOnlyView.as_view(), name='organizer-dashboard'),
    path('volunteer/', VolunteerOnlyView.as_view(), name='volunteer-dashboard'),
]
'''from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permissions', views.PermissionViewSet)
urlpatterns = [
    path('', include(router.urls)),'''