from django.shortcuts import render


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Status
from .serializers import StatusSerializer


class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]
