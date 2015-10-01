# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150922_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
