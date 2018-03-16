from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    """
    Abstract Model for defining created and modified timestamps for inherited models.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
