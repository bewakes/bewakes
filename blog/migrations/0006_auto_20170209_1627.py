# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 16:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170208_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 16, 27, 45, 893229)),
        ),
    ]