# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20150912_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_apply_method',
            field=models.CharField(default=b'draft', max_length=b'20', choices=[(b'link', b'Link'), (b'email', b'Email')]),
        ),
    ]
