# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-24 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('subtitle', models.CharField(max_length=255, null=True, verbose_name='subtitle')),
                ('amount', models.CharField(max_length=255, null=True, verbose_name='amount')),
                ('age', models.CharField(max_length=255, null=True, verbose_name='age')),
                ('appoitment', models.CharField(max_length=255, null=True, verbose_name='appoitment')),
                ('skin', models.CharField(max_length=255, null=True, verbose_name='skin')),
                ('frequency', models.CharField(max_length=255, null=True, verbose_name='frequency')),
                ('perfume', models.CharField(max_length=255, null=True, verbose_name='perfume')),
                ('consistency', models.CharField(max_length=255, null=True, verbose_name='consistency')),
                ('packaging', models.CharField(max_length=255, null=True, verbose_name='packaging')),
                ('country', models.CharField(max_length=255, null=True, verbose_name='country')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/')),
                ('description', redactor.fields.RedactorField(blank=True, null=True, verbose_name='text')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
