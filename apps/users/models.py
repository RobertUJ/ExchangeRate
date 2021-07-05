"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from apps.utils.models import ExchangeModel


class User(ExchangeModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
            'email address',
            unique=True,
            error_messages={
                'unique': 'A user with that email already exists.'
            }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_activated = models.BooleanField(
        'user status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username as short name"""
        return self.username
