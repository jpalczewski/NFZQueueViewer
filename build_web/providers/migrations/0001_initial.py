# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('NFZDepartment', models.DecimalField(max_digits=2, decimal_places=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('RelatedProvider', models.ForeignKey(to='providers.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='Provision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Urgent', models.BooleanField()),
                ('AverageWaitingDays', models.PositiveSmallIntegerField()),
                ('WaitingCustomers', models.PositiveSmallIntegerField()),
                ('ServedCustomers', models.PositiveSmallIntegerField()),
                ('FirstAvailableDate', models.DateField()),
                ('RelatedProviderSection', models.ForeignKey(to='providers.ProviderSection')),
            ],
        ),
    ]
