from rest_framework import permissions

class NoDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite todas as ações, exceto a exclusão
        if request.method == 'DELETE':
            return False
        return True
