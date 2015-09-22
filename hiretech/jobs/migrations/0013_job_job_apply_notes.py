# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_apply_notes',
            field=models.TextField(default=b''),
        ),
    ]
