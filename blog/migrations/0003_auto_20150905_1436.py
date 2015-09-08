# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
