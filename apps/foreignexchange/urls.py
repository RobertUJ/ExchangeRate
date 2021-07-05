"""Foreign Exchange URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.foreignexchange.views import ForeignExchangeViewSet

router = DefaultRouter()
router.register(r'foreign_exchange', ForeignExchangeViewSet, basename='foreign_exchange')

urlpatterns = [
    path('', include(router.urls))
]
