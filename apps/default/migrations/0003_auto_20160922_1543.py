# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-22 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20160922_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='id_endereco',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='default.Endereco'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_endereco',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='default.Endereco'),
        ),
    ]