# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_auto_20151004_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 4, 22, 30, 901217)),
        ),
    ]
