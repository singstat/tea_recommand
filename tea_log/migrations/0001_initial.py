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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tea', models.CharField(null=True, blank=True, max_length=50)),
                ('comment', models.TextField(null=True, blank=True)),
                ('like', models.BooleanField(default=True, choices=[(True, 'Like'), (False, 'Dislike')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nation', models.CharField(default='CH', max_length=10, choices=[('CH', 'Chinese'), ('JA', 'Japanese'), ('ID', 'India'), ('NE', 'Nepalese'), ('CY', 'Cylon'), ('TW', 'Twiwanese'), ('KO', 'Korea')])),
                ('color', models.CharField(default='OO', max_length=10, choices=[('GR    ', 'Green'), ('BL    ', 'Black'), ('WH    ', 'White'), ('OO    ', 'Oolong'), ('PU-ERH', 'Pu-erh'), ('PURPLE', 'Purple'), ('BLENED', 'Blened')])),
                ('status', models.CharField(default='le', max_length=10, choices=[('le', 'Leaf'), ('tg', 'Tea bag')])),
                ('company', models.ForeignKey(to='tea_log.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TeaName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='tea',
            name='name',
            field=models.ForeignKey(to='tea_log.TeaName'),
        ),
        migrations.AddField(
            model_name='tea',
            name='region',
            field=models.ForeignKey(to='tea_log.Region'),
        ),
    ]
