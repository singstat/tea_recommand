# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0004_auto_20150914_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_structure',
            name='Grade',
            field=models.CharField(choices=[(1, 'Like'), (0, 'Dislike')], max_length=10, default=1),
        ),
    ]
