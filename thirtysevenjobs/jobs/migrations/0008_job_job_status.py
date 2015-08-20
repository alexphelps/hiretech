# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_job_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_status',
            field=models.CharField(default=0, max_length=b'20', choices=[(0, b'Draft'), (1, b'Pending Review'), (2, b'Published'), (3, b'Filled')]),
        ),
    ]
