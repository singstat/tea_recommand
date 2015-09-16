# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='region',
            field=models.CharField(max_length=20, choices=[('An    ', 'Anxi        '), ('Guang ', 'Guangdong   '), ('Wu    ', 'WuYiMountain'), ('Yun   ', 'Yunnan      '), ('Dar   ', 'Darjeeling  '), ('ASS   ', 'Assam  '), ('Un    ', 'Unknown')], default='Un'),
        ),
    ]
