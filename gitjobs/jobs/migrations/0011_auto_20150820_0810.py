# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20150820_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
