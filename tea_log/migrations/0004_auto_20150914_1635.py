# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0003_auto_20150914_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_structure',
            name='Grade',
            field=models.IntegerField(choices=[(0, 'Like'), (1, 'Dislike')], default=1),
        ),
    ]
