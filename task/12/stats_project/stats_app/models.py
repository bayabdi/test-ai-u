from django.db import models


class Statistic(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()
