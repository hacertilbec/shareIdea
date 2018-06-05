# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class userProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    surname = models.CharField(max_length=100, blank=True, default='')
<<<<<<< HEAD
    department = models.CharField(max_length=100, blank=True, default='')
    statement = models.CharField(max_length=500, blank=True, default='')
    qualifications = models.CharField(max_length=500, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, default='')
    password = models.CharField(max_length=500, blank=True, default='')



    def __str__(self):
        return self.name+" "+self.surname

    class Meta:
        ordering = ('created',)

class Project(models.Model):
    owner = models.ManyToManyField(userProfile,related_name = "namee")
    participant = models.ManyToManyField(userProfile, related_name="name2")
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')
    language = models.CharField(max_length=100, blank=True, default='')
    starred_comment = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
=======
    school = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    personal_statement = models.CharField(max_length=500)
    qualifications = models.CharField(max_length=500)
>>>>>>> origin/master

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

