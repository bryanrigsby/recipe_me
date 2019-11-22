# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-20 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thanksgiving_recipes_app', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_has_comments', to='thanksgiving_recipes_app.User'),
        ),
    ]