# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_structure',
            name='Color',
            field=models.CharField(default='OO', max_length=10, choices=[('GR    ', 'Green'), ('BL    ', 'Black'), ('WH    ', 'White'), ('OO    ', 'Oolong'), ('PU-ERH', 'Pu-erh'), ('PURPLE', 'Purple'), ('BLENED', 'Blened')]),
        ),
        migrations.AlterField(
            model_name='log_structure',
            name='Nation',
            field=models.CharField(default='CH', max_length=10, choices=[('CH', 'Chinese'), ('JA', 'Japanese'), ('ID', 'India'), ('NE', 'Nepalese'), ('CY', 'Cylon'), ('TW', 'Twiwanese')]),
        ),
        migrations.AlterField(
            model_name='log_structure',
            name='Region',
            field=models.CharField(default='Un', max_length=10, choices=[('An    ', 'Anxi        '), ('Guang ', 'Guangdong   '), ('Wu    ', 'WuYiMountain'), ('Yun   ', 'Yunnan      '), ('Dar   ', 'Darjeeling  '), ('ASS   ', 'Assam  '), ('Un    ', 'Unknown')]),
        ),
    ]
