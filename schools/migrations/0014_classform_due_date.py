# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0013_studentform_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='classform',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
