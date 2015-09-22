# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_job_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='author',
            new_name='job_author',
        ),
    ]
