# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
