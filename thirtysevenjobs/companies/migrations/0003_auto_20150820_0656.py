# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150820_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_url',
            field=models.URLField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
