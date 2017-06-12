# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-15 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, null=True, verbose_name='content')),
                ('customer_name', models.CharField(max_length=255, null=True, verbose_name='customer_name')),
                ('customer_adress', models.CharField(max_length=255, null=True, verbose_name='customer_adress')),
                ('customer_phone', models.CharField(max_length=255, null=True, verbose_name='customer_phone')),
                ('customer_email', models.CharField(max_length=255, null=True, verbose_name='customer_email')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sale',
            },
        ),
    ]