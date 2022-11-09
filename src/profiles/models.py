from django.contrib.auth.models import AbstractUser
from django.db import models


class DigitalUser(AbstractUser):
    """Расширение модели пользователя"""
    ROLE = (
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('administrator', 'Администратор')
    )
    role = models.CharField(max_length=20, choices=ROLE)

    REQUIRED_FIELDS = ['role']
