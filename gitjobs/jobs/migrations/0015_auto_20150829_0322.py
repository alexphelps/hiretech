# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20150824_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_qualifications',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='job',
            name='job_responsibilities',
            field=models.TextField(default=b''),
        ),
    ]
