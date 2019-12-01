from django.contrib import admin

from .models import Package, Maintainer


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    pass


@admin.register(Maintainer)
class MaintainerAdmin(admin.ModelAdmin):
    pass
