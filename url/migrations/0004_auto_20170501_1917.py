# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0003_auto_20170501_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='endpoint',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='short_name',
            field=models.CharField(default='W2D6IcY4', max_length=8),
        ),
    ]
