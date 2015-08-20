# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_job_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_pub_date',
        ),
        migrations.AddField(
            model_name='job',
            name='job_created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.CharField(default=b'draft', max_length=b'20', choices=[(b'draft', b'Draft'), (b'pending_review', b'Pending Review'), (b'published', b'Published'), (b'filled', b'Filled')]),
        ),
    ]
