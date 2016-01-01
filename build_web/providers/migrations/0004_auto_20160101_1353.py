# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_provision_urgentapplicable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providersection',
            name='Phone',
            field=models.CharField(max_length=30),
        ),
    ]
