from django.db import models
from django.contrib.auth.models import User

class Cadet(models.Model):
    name = models.CharField(max_length=100)
    class_year = models.IntegerField()
    authos = models.CharField(max_length=3)

    def __str__(self):
        return self.name