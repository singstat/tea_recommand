# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_structure',
            name='Nation',
            field=models.CharField(choices=[('CH', 'Chinese'), ('JA', 'Japanese'), ('ID', 'India'), ('NE', 'Nepalese'), ('CY', 'Cylon'), ('TW', 'Twiwanese')], default='CH', max_length=10),
        ),
    ]
