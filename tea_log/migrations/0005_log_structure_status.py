# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0004_log_structure_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='Status',
            field=models.CharField(max_length=10, default='le', choices=[('le', 'Leaf'), ('tg', 'Tea bag')]),
        ),
    ]
