from django.db import models


class Status(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return str(self.timestamp) + ' ' + str(self.value)