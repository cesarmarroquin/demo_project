# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 05:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0025_studentattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
