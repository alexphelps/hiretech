# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0031_auto_20151010_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_created_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_expiration_date',
        ),
    ]
