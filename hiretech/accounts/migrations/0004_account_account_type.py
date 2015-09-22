# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150912_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default=b'employer', max_length=20, choices=[(b'employer', b'Employer'), (b'applicant', b'Applicant')]),
        ),
    ]
