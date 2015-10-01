# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_account_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='paid',
        ),
        migrations.AddField(
            model_name='account',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]
