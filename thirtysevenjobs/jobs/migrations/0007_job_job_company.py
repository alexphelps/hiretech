# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150820_0638'),
        ('jobs', '0006_auto_20150820_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_company',
            field=models.ForeignKey(default=0, to='companies.Company'),
        ),
    ]
