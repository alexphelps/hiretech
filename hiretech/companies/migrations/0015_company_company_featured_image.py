# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0014_company_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_featured_image',
            field=models.ImageField(default=b'', upload_to=b'media'),
        ),
    ]
