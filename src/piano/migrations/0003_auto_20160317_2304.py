# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0002_song_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='composer',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 3, 17, 23, 4, 0, 591815, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
