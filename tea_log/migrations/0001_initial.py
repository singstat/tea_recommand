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
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, unique=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('like', models.BooleanField(choices=[(True, 'Like'), (False, 'Dislike')], default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nation', models.CharField(max_length=10, choices=[('CH', 'Chinese'), ('JA', 'Japanese'), ('ID', 'India'), ('NE', 'Nepalese'), ('CY', 'Cylon'), ('TW', 'Twiwanese'), ('KO', 'Korea'), ('Un    ', 'Unknown')], default='CH')),
                ('region', models.CharField(max_length=20, choices=[('An    ', 'Anxi        '), ('Guang ', 'Guangdong   '), ('Wu    ', 'WuYiMountain'), ('Yun   ', 'Yunnan      '), ('Dar   ', 'Darjeeling  '), ('ASS   ', 'Assam  '), ('Un    ', 'Unknown')], default='Un', unique=True)),
                ('color', models.CharField(max_length=10, choices=[('GR    ', 'Green'), ('BL    ', 'Black'), ('WH    ', 'White'), ('OO    ', 'Oolong'), ('PU-ERH', 'Pu-erh'), ('PURPLE', 'Purple'), ('BLENED', 'Blened')], default='OO')),
                ('status', models.CharField(max_length=10, choices=[('le', 'Leaf'), ('tg', 'Tea bag')], default='le')),
                ('company', models.ForeignKey(to='tea_log.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TeaName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, unique=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='tea',
            name='name',
            field=models.ForeignKey(to='tea_log.TeaName'),
        ),
        migrations.AddField(
            model_name='entry',
            name='tea_info',
            field=models.ForeignKey(null=True, to='tea_log.Tea'),
        ),
    ]
