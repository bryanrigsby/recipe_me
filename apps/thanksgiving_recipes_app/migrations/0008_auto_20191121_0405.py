# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanksgiving_recipes_app', '0007_auto_20191121_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cook_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='hours',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cost',
            field=models.IntegerField(),
        ),
    ]
