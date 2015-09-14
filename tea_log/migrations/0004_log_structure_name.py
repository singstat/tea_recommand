# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0003_log_structure_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='name',
            field=models.CharField(default='NULL', max_length=50),
        ),
    ]
