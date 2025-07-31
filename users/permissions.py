from rest_framework import permissions

class IsOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ORGANIZER'

class IsVolunteer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'VOLUNTEER'