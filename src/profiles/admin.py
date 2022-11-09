from django.contrib import admin

from . import models


@admin.register(models.DigitalUser)
class DigitalUser(admin.ModelAdmin):
    pass
