# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='short_name',
            field=models.CharField(default='hjiw43es', max_length=8),
            preserve_default=False,
        ),
    ]
