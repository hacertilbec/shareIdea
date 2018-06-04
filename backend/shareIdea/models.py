# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class userProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    surname = models.CharField(max_length=100, blank=True, default='')
    school = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    personal_statement = models.CharField(max_length=500)
    qualifications = models.CharField(max_length=500)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Project(models.Model):
    owner = models.ManyToManyField(userProfile)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    stored_count = models.IntegerField()
    date = models.DateTimeField(max_length=250)

    def __str__(self):
        return self.title

