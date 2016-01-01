# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20160101_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='provision',
            name='UrgentApplicable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
