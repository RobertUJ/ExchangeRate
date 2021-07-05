"""Foreign exchange model admin."""

# Django
from django.contrib import admin

# Models
from apps.foreignexchange.models import ForeignExchange


class ExchangeModelAdmin(admin.ModelAdmin):
    """Foreign Change model admin."""

    list_display = ('value', 'provider', 'created')
    list_filter = ('provider', 'created')


admin.site.register(ForeignExchange, ExchangeModelAdmin)
