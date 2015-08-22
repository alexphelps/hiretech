# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20150820_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default=b'full_time', max_length=20, choices=[(b'full_time', b'Full Time'), (b'part_time', b'Part Time'), (b'contract', b'Contract'), (b'internship', b'Internship')]),
        ),
    ]
