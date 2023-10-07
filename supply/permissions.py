from rest_framework.permissions import BasePermission


class CustomAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:    # Разрешить все операции для аутентифицированных пользователей
            return True
        return False