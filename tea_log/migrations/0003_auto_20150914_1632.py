# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0002_auto_20150914_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='Grade',
            field=models.BinaryField(choices=[(0, 'Like'), (1, 'Dislike')], default=1),
        ),
        migrations.AddField(
            model_name='log_structure',
            name='Status',
            field=models.CharField(choices=[('le', 'Leaf'), ('tg', 'Tea bag')], default='le', max_length=10),
        ),
    ]
