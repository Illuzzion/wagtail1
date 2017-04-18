# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 11:00
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0009_blogcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'Категории блога'},
        ),
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='newblog.BlogCategory'),
        ),
    ]
