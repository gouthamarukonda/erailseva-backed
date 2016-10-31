# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Message')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('cust_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
