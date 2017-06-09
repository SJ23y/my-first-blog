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
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField()),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tittle', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='question_like_user')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='qa.Question'),
        ),
    ]
