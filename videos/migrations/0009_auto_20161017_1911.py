# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20161017_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimage',
            name='image',
            field=models.ImageField(upload_to='/Users/jiawu/Desktop/venv/myproject/myproject/static/img/category_img'),
        ),
        migrations.AlterField(
            model_name='videoimage',
            name='image',
            field=models.ImageField(upload_to='/Users/jiawu/Desktop/venv/myproject/myproject/static/img/video_img'),
        ),
    ]
