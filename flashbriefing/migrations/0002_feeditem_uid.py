# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashbriefing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeditem',
            name='uid',
            field=models.CharField(default='1234', max_length=255),
            preserve_default=False,
        ),
    ]