"""Banxico get rates."""

import requests

# Models
from apps.foreignexchange.models import ForeignExchange

# Celery
from celery import Celery
app = Celery()

TOKEN = 'e58256aaafc6beb774cbcaa21d964700997babda499b63868867003d4ad2f797'
IDSERIES = 'SF43718'
URL = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/{IDSERIES}/datos/oportuno?token={TOKEN}'


# @app.task
def get_rates_banxico():
    """Get data foreignexchange from banxico provider."""
    req = requests.get(URL)
    if req.status_code == 200:
        usd_mxn_val = None
        try:
            data = req.json()
            series_key = data.get('bmx', {}).get('series', None)
            if series_key is not None and len(series_key) > 0:
                datos_key = series_key[0].get('datos', [])
                if len(datos_key) > 0:
                    usd_mxn_val = datos_key[0].get('dato', None)
                    if usd_mxn_val is not None:
                        ForeignExchange.objects.create(
                            provider='prov_3',
                            value=usd_mxn_val
                        )

        finally:
            pass
