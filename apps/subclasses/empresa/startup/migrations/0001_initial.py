# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-22 15:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('default', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalStartup',
            fields=[
                ('id_startup', models.IntegerField(blank=True, db_index=True)),
                ('representante', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('logo', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagem')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('empresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='default.Empresa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical startup',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id_startup', models.AutoField(primary_key=True, serialize=False)),
                ('representante', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/subclasses/empresa/', verbose_name='Imagem')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='startup_name', to='default.Empresa')),
            ],
        ),
    ]
