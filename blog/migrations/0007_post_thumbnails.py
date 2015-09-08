# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnails',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
