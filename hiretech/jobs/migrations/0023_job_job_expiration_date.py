# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_auto_20150921_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 9, 20, 44, 502045)),
        ),
    ]
