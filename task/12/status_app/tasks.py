# status_app/tasks.py

import random
from celery import shared_task
from datetime import datetime, timedelta, timezone
import requests
from .models import Status


@shared_task
def add_random_status():
    Status.objects.create(
        timestamp=datetime.now(),
        value=float(random.randint(1, 100))
    )
    url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo'
    r = requests.get(url)
    data = r.json()

    timestamp = timezone.now()
    value = data['payload']['RETURNS_CALCULATIONS']['MEAN']['IBM']

    print("Status added!")
