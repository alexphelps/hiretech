# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20150908_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_user',
        ),
    ]
