from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=120)
    message = models.CharField(max_length=600)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title