# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 08:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0034_auto_20160101_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolevent',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]