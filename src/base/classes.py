class MixedPermission:
    """Миксин действия разрешений"""

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class MixedSerializer:
    """Миксин действия сериализатора"""

    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class MixedPermissionSerializer(MixedPermission, MixedSerializer):
    """ Разрешения и миксин действия сериализатора"""
    pass
