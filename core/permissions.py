from rest_framework import permissions
class UserPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        elif view.action == 'list':
            return obj == request.user or request.user.is_admin
        elif view.action == 'retrieve':
            return obj == request.user or request.user.is_admin
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_admin
        elif view.action == 'destroy':
            return obj == request.user.is_superuser or request.user.is_staff
        return obj == request.user
