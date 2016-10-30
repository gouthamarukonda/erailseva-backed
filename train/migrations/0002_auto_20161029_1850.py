# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_no', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name=b'Train No')),
                ('train_name', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Train Name')),
                ('start_time', models.TimeField(auto_now=True, verbose_name=b'Start Time')),
                ('end_time', models.TimeField(auto_now=True, verbose_name=b'End Time')),
                ('time_stamp', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('from_station_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_station_train', to='station.Station')),
                ('to_station_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_station_train', to='station.Station')),
            ],
        ),
        migrations.DeleteModel(
            name='TrainModel',
        ),
    ]
