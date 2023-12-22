from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Statistic
from datetime import timezone, timedelta


@csrf_exempt
def statistics_endpoint(request):
    last_24_hours = Statistic.objects.filter(timestamp__gte=timezone.now() - timedelta(days=1))

    data = [{'timestamp': stat.timestamp, 'value': stat.value} for stat in last_24_hours]

    return JsonResponse({'data': data})
