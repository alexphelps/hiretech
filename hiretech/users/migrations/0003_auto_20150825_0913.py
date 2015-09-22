# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(default=b'employer', max_length=20, choices=[(b'employer', b'Employer'), (b'applicant', b'Applicant'), (b'agent', b'Agent')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(default=b'', to='companies.Company'),
        ),
    ]
