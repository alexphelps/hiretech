# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20150829_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_apply_notes',
            new_name='job_notes',
        ),
    ]
