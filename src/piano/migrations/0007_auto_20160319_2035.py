# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0006_song_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='books',
            field=models.ForeignKey(default=1, to='piano.Book'),
        ),
        migrations.AlterField(
            model_name='song',
            name='level',
            field=models.CharField(default=1, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='period',
            field=models.CharField(default=b'DEFAULT', max_length=20, choices=[(b'B', b'Baroque'), (b'C', b'Classical'), (b'R', b'Romantic'), (b'M', b'Modern')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
