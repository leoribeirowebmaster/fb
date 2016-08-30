# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20, null=True, blank=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='funcionario_name')),
            ],
        ),
    ]
