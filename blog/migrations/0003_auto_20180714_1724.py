# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=40, unique=True),
        ),
    ]