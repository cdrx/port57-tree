from __future__ import unicode_literals

from django.db import models


class Colour(models.Model):
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name or u""

