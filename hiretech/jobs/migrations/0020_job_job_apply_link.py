# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_job_job_apply_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_apply_link',
            field=models.CharField(default=b'', max_length=400),
        ),
    ]
