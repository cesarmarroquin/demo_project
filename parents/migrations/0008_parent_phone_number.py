# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 00:22
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0007_parent_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True),
        ),
    ]
