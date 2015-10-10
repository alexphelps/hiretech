# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0032_auto_20151010_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 5, 22, 56, 750540, tzinfo=utc)),
        ),
    ]
