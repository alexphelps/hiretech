# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_job_job_apply_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=b''),
        ),
    ]
