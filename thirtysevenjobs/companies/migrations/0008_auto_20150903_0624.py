# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='slug',
            new_name='company_slug',
        ),
    ]
