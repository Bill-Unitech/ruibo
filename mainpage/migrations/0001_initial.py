# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=120)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
    ]
