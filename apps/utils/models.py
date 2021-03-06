"""Django models utilities."""

# Django
from django.db import models


class ExchangeModel(models.Model):
    """Exchange Rate base model.

    Exchange Model acts as an abstract base class from which every other model in the 
    project will inherit. 
    This class provides every table with the following attributes:
        + created (DateTime): Store the last datetime the object was created. 
        + modified (DateTime): Store the las datetime the object was modified.
    """

    created = models.DateTimeField(
            'created at',
            auto_now_add=True,
            help_text='Date time on wich the object was created.'
    )

    modified = models.DateTimeField(
            'modified at',
            auto_now_add=True,
            help_text='Date time on wich the object was las modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

