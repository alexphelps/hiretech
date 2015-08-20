# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150820_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=0, to='jobs.Category'),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.ForeignKey(default=0, to='jobs.Location'),
        ),
    ]
