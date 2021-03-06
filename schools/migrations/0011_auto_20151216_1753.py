# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_classfeepayment_amount_needed'),
    ]

    operations = [
        migrations.AddField(
            model_name='classfeepayment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='classfeepayment',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='classfeepayment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='class_fee_images'),
        ),
        migrations.AddField(
            model_name='classfeepayment',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
