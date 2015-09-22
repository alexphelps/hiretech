# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_account_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
