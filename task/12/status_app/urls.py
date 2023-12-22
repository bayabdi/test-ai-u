from django.urls import path
from .views import StatusList

urlpatterns = [
    path('api/status/', StatusList.as_view(), name='status-list'),
]
