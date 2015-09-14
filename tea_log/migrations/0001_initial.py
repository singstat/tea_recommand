# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_structure',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Company', models.CharField(max_length=200)),
                ('Color', models.CharField(default='OO', choices=[('GR    ', 'Green'), ('BL    ', 'Black'), ('WH    ', 'White'), ('OO    ', 'Oolong'), ('PU-ERH', 'Pu-erh'), ('PURPLE', 'Purple'), ('BLENED', 'Blened')], max_length=10)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
