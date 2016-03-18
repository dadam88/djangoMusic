# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_song_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='period',
        ),
        migrations.AddField(
            model_name='song',
            name='myfield',
            field=models.CharField(default='hap', max_length=256, choices=[(b'green', b'green'), (b'red', b'red')]),
            preserve_default=False,
        ),
    ]
