# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0009_company_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(default=b'', upload_to=b'media'),
        ),
    ]
