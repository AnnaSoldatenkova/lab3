# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_name', models.CharField(max_length=100)),
                ('address_x', models.PositiveIntegerField()),
                ('address_y', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver_name', models.TextField(max_length=100)),
                ('phone_num', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=100)),
                ('client_phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaxiOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField()),
                ('car_id', models.ForeignKey(to='taxi.Car')),
                ('client_id', models.ForeignKey(to='taxi.Client')),
                ('finish_id', models.ForeignKey(related_name='finish', to='taxi.Address')),
                ('start_id', models.ForeignKey(related_name='start', to='taxi.Address')),
            ],
        ),
    ]
