# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150820_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
