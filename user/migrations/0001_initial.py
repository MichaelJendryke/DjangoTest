# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fistname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('affiliation', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('lastactive_date', models.DateTimeField(verbose_name='last date active')),
                ('birthday_date', models.DateTimeField(verbose_name='birthday')),
            ],
        ),
    ]
