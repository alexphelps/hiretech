# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20150820_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_created_date',
            field=models.DateTimeField(null=True, verbose_name=b'date created'),
        ),
    ]
