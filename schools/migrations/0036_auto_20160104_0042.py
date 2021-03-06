# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0035_auto_20160104_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classevent',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='classevent',
            name='description',
            field=models.TextField(default='class event description'),
        ),
        migrations.AlterField(
            model_name='schoolevent',
            name='description',
            field=models.TextField(default='school event description'),
        ),
    ]
