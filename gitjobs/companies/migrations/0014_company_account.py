# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150912_0503'),
        ('companies', '0013_auto_20150912_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='account',
            field=models.ForeignKey(blank=True, to='accounts.Account', null=True),
        ),
    ]
