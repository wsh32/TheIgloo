# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160418_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=15, unique=True)),
                ('password', models.TextField()),
            ],
        ),
    ]
