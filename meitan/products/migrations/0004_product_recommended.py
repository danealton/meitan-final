# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-15 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170321_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
