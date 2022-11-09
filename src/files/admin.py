from django.contrib import admin

from . import models


@admin.register(models.SPGZ)
class SPGZAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SN)
class SNAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TSN)
class TSNAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Template)
class SampleTZAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Estimate)
class EstimateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ResultFile)
class ResultFileAdmin(admin.ModelAdmin):
    pass
