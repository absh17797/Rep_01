# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms_App', '0002_auto_20190417_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
