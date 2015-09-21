# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
