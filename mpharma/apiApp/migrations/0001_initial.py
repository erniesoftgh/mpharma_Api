# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-06 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='icdCode',
            fields=[
                ('category_code', models.CharField(blank=True, max_length=90, null=True)),
                ('diagnosis_code', models.CharField(blank=True, max_length=300, null=True)),
                ('full_code', models.CharField(default='na', max_length=300, primary_key=True, serialize=False)),
                ('abbreviated_description', models.CharField(blank=True, max_length=300, null=True)),
                ('full_description', models.CharField(blank=True, max_length=300, null=True)),
                ('category_title', models.CharField(blank=True, max_length=300, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
