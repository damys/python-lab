# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-19 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]