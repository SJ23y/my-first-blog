# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]
