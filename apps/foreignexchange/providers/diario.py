"""Diario oficial get rates."""

import requests
from bs4 import BeautifulSoup

# Models
from apps.foreignexchange.models import ForeignExchange

# Celery
from celery import Celery
app = Celery()

URL = 'https://www.banxico.org.mx/tipcamb/tipCamMIAction.do'


# @app.task
def get_rates_diario():
    req = requests.get(URL)
    if req.status_code == 200:
        try:
            sopita = BeautifulSoup(req.text, 'lxml')
            tds = sopita.select('tr.renglonNon > td', limit=4)
            usd_mxn_val = float(tds[-1].get_text().strip())
            ForeignExchange.objects.create(
                provider='prov_1',
                value=usd_mxn_val
            )
        finally:

            pass
