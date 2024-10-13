"""Representation of models from sith_app in the admin interface."""
from django.contrib import admin

from recruitment.sith_app.models import Sith


@admin.register(Sith)
class SithAdmin(admin.ModelAdmin):
    """Representation of Sith model in the admin interface."""

    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_shadow_hand',
        'master',
        'age',
        'email',
        'planet',
    )
    search_fields = ('username',)
    list_filter = ('is_shadow_hand',)
