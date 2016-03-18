# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='level',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
