# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_remove_company_company_user'),
        ('users', '0007_userprofile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(default=b'', to='companies.Company'),
        ),
    ]
