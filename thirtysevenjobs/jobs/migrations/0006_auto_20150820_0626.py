# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_job_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='pub_date',
            new_name='job_pub_date',
        ),
    ]
