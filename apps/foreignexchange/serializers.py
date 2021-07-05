"""Foreign Exchange serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.foreignexchange.models import ForeignExchange


class ForeignExchangeSerializer(serializers.HyperlinkedModelSerializer):
    provider = serializers.CharField(source='get_provider_display')

    class Meta:
        model = ForeignExchange
        fields = ['provider', 'value', 'created']
