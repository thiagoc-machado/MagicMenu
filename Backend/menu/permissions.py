from rest_framework import permissions

class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifique se o usuário é um administrador
        return request.user and request.user.is_staff