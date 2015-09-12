# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='position',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='position',
            field=models.IntegerField(default=1),
        ),
    ]
