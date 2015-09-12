# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnails',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
