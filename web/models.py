from django.db import models

class Web(models.Model):
    name = models.CharField(max_length=100)
