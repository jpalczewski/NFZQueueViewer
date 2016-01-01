# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='provider',
            name='Name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='providersection',
            name='Address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='providersection',
            name='City',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='providersection',
            name='Name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='provision',
            name='Name',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='record',
            name='PS',
            field=models.ForeignKey(to='providers.ProviderSection'),
        ),
        migrations.AddField(
            model_name='record',
            name='Pn',
            field=models.ForeignKey(to='providers.Provision'),
        ),
        migrations.AddField(
            model_name='record',
            name='Pr',
            field=models.ForeignKey(to='providers.Provider'),
        ),
    ]
