# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0032_studentbehavior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbehavior',
            name='description',
            field=models.TextField(default='Behavior was good for today.'),
        ),
    ]
