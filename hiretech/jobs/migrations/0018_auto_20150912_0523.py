# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20150903_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True),
        ),
    ]
