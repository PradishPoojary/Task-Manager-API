from rest_framework import permissions

class IsOwnerOrManagerReadOnly(permissions.BasePermission):
    """
    Object-level permission: 
    - Safe methods (GET) are allowed if the user is the owner OR a manager.
    - Unsafe methods (PUT, DELETE) are ONLY allowed if the user is the owner.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read permissions if they are a manager
        if request.method in permissions.SAFE_METHODS and request.user.is_staff:
            return True
            
        # Write permissions are strictly isolated to the owner of the task
        return obj.user == request.user