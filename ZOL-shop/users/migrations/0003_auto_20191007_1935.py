# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-07 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190921_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
