# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-31 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythontips', '0002_auto_20190731_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='tip_link',
            field=models.IntegerField(default=1),
        ),
    ]
