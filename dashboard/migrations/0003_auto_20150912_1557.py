# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150910_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AddField(
            model_name='settings',
            name='slug',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
