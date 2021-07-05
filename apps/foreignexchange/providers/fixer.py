"""Fixer, provider to get exchange rate."""

import requests

# Models
from apps.foreignexchange.models import ForeignExchange
# Celery
from celery import Celery
app = Celery()

# Config
API_ACCESS = 'access_key=d6ab02457f01a9f3ffe1cb7e98397d38'
HOTS = 'http://data.fixer.io/api/latest?'
PARAMS = '&symbols=MXN,USD'
URL = f'{HOTS}{API_ACCESS}{PARAMS}'


# @app.task
def get_rates_fixer():
    """Get data foreignexchange from fixer provider."""
    req = requests.get(URL)
    data = req.json()
    if req.status_code == 200 and data['success'] is True:
        """Get and convert rate info."""
        eur_mxn_val = data['rates']['MXN']
        eur_usd_val = data['rates']['USD']
        usd_mxn_val = float(eur_mxn_val/eur_usd_val)
        ForeignExchange.objects.create(
            provider='prov_2',
            value=usd_mxn_val
        )
