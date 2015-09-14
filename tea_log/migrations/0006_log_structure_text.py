# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0005_log_structure_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
