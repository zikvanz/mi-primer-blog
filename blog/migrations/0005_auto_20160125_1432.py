# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160124_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.Post'),
        ),
    ]
