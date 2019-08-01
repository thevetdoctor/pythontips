# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tip(models.Model):
    tip_timestamp = models.DateTimeField()
    tip_text = models.CharField(max_length=200)
    tip_link = models.IntegerField(default=0)
    tip_author = models.CharField(max_length=20)
    tip_published = models.BooleanField(default=True)

    def __str__(self):
        return self.tip_text

    # def save()

    # def full(self):
    #     return '{} {} {} {}'.format(self.tip_text, self.tip_link, self.tip_author, self.tip_timestamp)

    # def __str__(self):
    #     return self.full()


class Link(models.Model):
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    # tip_count = models.IntegerField(default=1)

    def __str__(self):
        return self.link

