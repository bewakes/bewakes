# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170208_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 8, 21, 53, 287991)),
        ),
    ]
