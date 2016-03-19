# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0005_auto_20160317_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='period',
            field=models.CharField(default=b'DEFAULT', max_length=20, choices=[(b'Baroque', b'Baroque'), (b'Classical', b'Classical'), (b'Romantic', b'Romantic'), (b'Modern', b'Modern')]),
        ),
    ]
