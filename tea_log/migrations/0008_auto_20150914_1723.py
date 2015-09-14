# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0007_log_structure_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='log_structure',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
