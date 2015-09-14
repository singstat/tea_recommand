# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_structure',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Company', models.CharField(max_length=200)),
                ('Color', models.CharField(max_length=2, choices=[('GR    ', 'Green'), ('BL    ', 'Black'), ('WH    ', 'White'), ('OO    ', 'Oolong'), ('PU-ERH', 'Pu-erh'), ('PURPLE', 'Purple'), ('BLENED', 'Blened')], default='OO')),
                ('Nation', models.CharField(max_length=2, choices=[('CH', 'Chinese'), ('JA', 'Japanese'), ('ID', 'India'), ('NE', 'Nepalese'), ('CY', 'Cylon'), ('TW', 'Twiwanese')], default='CH')),
                ('Region', models.CharField(max_length=2, choices=[('An    ', 'Anxi        '), ('Guang ', 'Guangdong   '), ('Wu    ', 'WuYiMountain'), ('Yun   ', 'Yunnan      '), ('Dar   ', 'Darjeeling  '), ('Un    ', 'Unknown')], default='Un')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
