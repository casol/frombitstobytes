# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
