# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170207_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 4, 45, 13, 584771)),
        ),
    ]
