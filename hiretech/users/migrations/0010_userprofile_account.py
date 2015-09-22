# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150912_0503'),
        ('users', '0009_remove_userprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='account',
            field=models.ForeignKey(blank=True, to='accounts.Account', null=True),
        ),
    ]
