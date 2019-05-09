# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms_App', '0005_auto_20190423_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Ph_no', models.IntegerField()),
            ],
        ),
    ]
