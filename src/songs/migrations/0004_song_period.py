# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_song_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='period',
            field=models.CharField(default=b'none', max_length=15),
        ),
    ]
