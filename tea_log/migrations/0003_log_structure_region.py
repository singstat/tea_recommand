# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0002_log_structure_nation'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='Region',
            field=models.CharField(choices=[('An    ', 'Anxi        '), ('Guang ', 'Guangdong   '), ('Wu    ', 'WuYiMountain'), ('Yun   ', 'Yunnan      '), ('Dar   ', 'Darjeeling  '), ('ASS   ', 'Assam  '), ('Un    ', 'Unknown')], default='Un', max_length=10),
        ),
    ]
