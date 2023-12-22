from django.urls import path
from .views import statistics_endpoint

urlpatterns = [
    path('api/statistics/', statistics_endpoint, name='statistics_endpoint'),
]
