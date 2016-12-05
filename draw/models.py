from __future__ import unicode_literals
import uuid

from django.db import models


class Drawing(models.Model):
    valid_to = models.DateTimeField()
    token = models.UUIDField(default=uuid.uuid4)
    data = models.TextField()

    def __unicode__(self):
        return str(self.token)
