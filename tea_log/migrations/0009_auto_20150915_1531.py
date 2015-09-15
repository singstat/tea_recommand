# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0008_auto_20150914_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_structure',
            name='Grade',
            field=models.BooleanField(default=True, choices=[(True, 'Like'), (False, 'Dislike')]),
        ),
        migrations.AlterField(
            model_name='log_structure',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
