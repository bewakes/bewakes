# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170204_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 7, 21, 12, 51, 533134)),
        ),
    ]
