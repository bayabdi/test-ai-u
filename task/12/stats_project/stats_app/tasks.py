# stats_app/tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Statistic
import requests


@shared_task
def collect_statistics():
    url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo'
    r = requests.get(url)
    data = r.json()

    timestamp = timezone.now()
    value = data['payload']['RETURNS_CALCULATIONS']['MEAN']['IBM']

    Statistic.objects.create(timestamp=timestamp, value=value)
