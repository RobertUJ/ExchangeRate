"""Foreign Exchange Model."""

# Django
from django.db import models

# ExchangeRate utilities model
from apps.utils.models import ExchangeModel


class ForeignExchange(ExchangeModel):
    """Foreign Exchange Rate model."""

    PROVIDERS = (
        ('prov_1', 'Diario oficial de la federación'),
        ('prov_2', 'Fixer'),
        ('prov_3', 'Banxico')
    )

    provider = models.CharField(
        max_length=48,
        choices=PROVIDERS,
        help_text='A list of authorized providers'
    )
    value = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    @property
    def get_value(self):
        return f'${self.value}'

    def __str__(self):
        """Return foreign exchange str representation."""
        return f'{self.value}'
