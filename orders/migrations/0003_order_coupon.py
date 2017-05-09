# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_coupon_active'),
        ('orders', '0002_auto_20170503_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='coupons.Coupon'),
        ),
    ]
