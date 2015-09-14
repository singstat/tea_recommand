# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0006_log_structure_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='Grade',
            field=models.CharField(default='L', choices=[('L', 'Like'), ('D', 'Dislike')], max_length=10),
        ),
    ]
