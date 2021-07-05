"""Task celery setup."""

# Celery
from exchangerate.celery import app

# Methods to get rates from providers
from apps.foreignexchange.providers import get_rates_banxico, get_rates_fixer, get_rates_diario


@app.task(name='tasks.fixer')
def rates_fixer():
    print("get rates to fixer")
    get_rates_fixer()


@app.task(name='tasks.diario')
def rates_diario():
    print("get rates to diario oficial")
    get_rates_diario()


@app.task(name='tasks.banxico')
def rates_banxico():
    print("get rates to banxico")
    get_rates_banxico()
