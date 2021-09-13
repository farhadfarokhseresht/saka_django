from django.contrib import admin
from . import models


@admin.register(models.Tmethod)
class Tmethod_admin(admin.ModelAdmin):
    list_display =  [field.name for field in models.Tmethod._meta.get_fields()]


@admin.register(models.Device)
class Device_admin(admin.ModelAdmin):
    list_display =  [field.name for field in models.Device._meta.get_fields()]


@admin.register(models.Devicecompany)
class Devicecompany_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Devicecompany._meta.get_fields()]


@admin.register(models.InfoDevice)
class InfoDevice_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.InfoDevice._meta.get_fields()]


@admin.register(models.Info)
class ModelAdmin_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Info._meta.get_fields()]


@admin.register(models.Facttable)
class Facttable_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Facttable._meta.get_fields()]


@admin.register(models.Laboratory)
class Laboratory_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Laboratory._meta.get_fields()]


@admin.register(models.Analyte)
class Analyte_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Analyte._meta.get_fields()]


@admin.register(models.Cash)
class Cash_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Cash._meta.get_fields()]


@admin.register(models.InfoTD)
class InfoTD_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.InfoTD._meta.get_fields()]


@admin.register(models.InfoTmethod)
class InfoTmethod_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.InfoTmethod._meta.get_fields()]


@admin.register(models.Latnumber)
class Latnumber_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Latnumber._meta.get_fields()]


@admin.register(models.Singup)
class Singup_admin(admin.ModelAdmin):
    list_display = [field.name for field in models.Singup._meta.get_fields()]

