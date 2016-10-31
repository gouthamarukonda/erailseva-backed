# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='Shop id')),
                ('shop_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Shop Name')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('station_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.Station')),
            ],
        ),
    ]
