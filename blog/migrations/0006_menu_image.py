# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150906_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
