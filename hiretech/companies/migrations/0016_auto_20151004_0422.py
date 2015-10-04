# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_company_company_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_featured_image',
            field=models.ImageField(default=b'', upload_to=b'media', blank=True),
        ),
    ]
