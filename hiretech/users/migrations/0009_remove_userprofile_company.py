# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150908_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
    ]
