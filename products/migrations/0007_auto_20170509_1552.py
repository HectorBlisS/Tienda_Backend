# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_document_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='users',
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]