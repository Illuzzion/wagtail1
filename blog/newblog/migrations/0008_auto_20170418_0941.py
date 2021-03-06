# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0007_auto_20170418_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(max_length=250),
        ),
    ]
