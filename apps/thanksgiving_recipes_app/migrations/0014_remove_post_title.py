# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thanksgiving_recipes_app', '0013_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
