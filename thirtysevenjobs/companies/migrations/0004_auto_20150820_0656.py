# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150820_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_url',
            field=models.URLField(default=b''),
        ),
    ]
