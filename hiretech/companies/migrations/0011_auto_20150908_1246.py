# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0010_auto_20150908_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_user',
        ),
        migrations.AddField(
            model_name='company',
            name='company_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
