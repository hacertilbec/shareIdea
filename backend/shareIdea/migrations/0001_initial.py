# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('userId', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('surname', models.CharField(blank=True, default='', max_length=100)),
                ('school', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
