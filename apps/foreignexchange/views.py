"""Foreign Exchange Views."""
# Django
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# REST Framework
from django.db.models import Max, F
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

# Models
from apps.foreignexchange.models import ForeignExchange

# Serializers
from apps.foreignexchange.serializers import ForeignExchangeSerializer


@method_decorator(never_cache, name='dispatch')
class ForeignExchangeViewSet(viewsets.ModelViewSet):
    queryset = ForeignExchange.objects.all().order_by('provider', '-created').distinct('provider')
    serializer_class = ForeignExchangeSerializer
    permission_classes = [IsAuthenticated, ]
    throttle_classes = [UserRateThrottle, ]
