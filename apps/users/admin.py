"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from apps.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_activated')
    list_filter = ('is_activated', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
