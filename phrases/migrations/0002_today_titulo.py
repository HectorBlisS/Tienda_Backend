# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='today',
            name='titulo',
            field=models.CharField(default='frase de hoy', max_length=140),
            preserve_default=False,
        ),
    ]
