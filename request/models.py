from __future__ import unicode_literals

from django.db import models

from colour.models import Colour


class ColourRequest(models.Model):
    source = models.CharField(max_length=100, default="Manual")
    user = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    colour = models.ForeignKey(Colour)

    requested = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-requested', ]
        get_latest_by = 'requested'

