# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-28 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_learning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning',
            name='lenrnType',
        ),
        migrations.AddField(
            model_name='learning',
            name='learnType',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='learning',
            name='webName',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
