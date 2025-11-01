"""Representation of models from main_app in the admin interface."""
from django.contrib import admin

from recruitment.main_app.models import CustomUser, Planet


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Representation of CustomUser model in the admin interface."""

    list_display = (
        'username',
        'first_name',
        'last_name',
        'age',
        'email',
        'role',
    )
    list_filter = ('role',)
    search_fields = ('username',)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    """Representation of Planet model in the admin interface."""

    list_display = ('name', 'description')
    list_filter = ('name',)
