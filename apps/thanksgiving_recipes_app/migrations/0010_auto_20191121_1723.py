# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanksgiving_recipes_app', '0009_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
