from rest_framework.permissions import IsAuthenticated


class IsAuthor(IsAuthenticated):
    """Автор объекта"""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsModerator(IsAuthenticated):
    """Модератор"""

    def has_object_permission(self, request, view, obj):
        if request.user.role == "moderator":
            return True


class IsAdministrator(IsAuthenticated):
    """Администратор"""

    def has_object_permission(self, request, view, obj):
        if request.user.role == "administrator":
            return True
