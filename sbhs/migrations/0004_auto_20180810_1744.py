# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbhs', '0003_auto_20180810_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbhs.Slot'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]