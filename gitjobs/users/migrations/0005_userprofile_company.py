# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_remove_company_company_user'),
        ('users', '0004_auto_20150908_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(default=b'', to='companies.Company'),
        ),
    ]
