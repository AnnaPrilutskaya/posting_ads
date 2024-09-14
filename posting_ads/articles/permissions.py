from rest_framework import permissions  

class IsAuthorOrReadOnlyPermission(permissions.BasePermission): 

    def has_object_permission(self, request, view, obj): 
        if request.user.is_authenticated: 
            return ( 
                request.method in permissions.SAFE_METHODS 
                or obj.author == request.user 
            ) 
        return request.method in permissions.SAFE_METHODS
    

'''class IsAdmin(permissions.BasePermission):
    """Для admin и superuser."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin)'''