# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='picture_url',
            field=models.URLField(default='http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png'),
        ),
    ]
