# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150820_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='category',
            new_name='job_category',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='job_location',
        ),
    ]
