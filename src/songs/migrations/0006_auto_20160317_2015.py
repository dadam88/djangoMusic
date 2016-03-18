# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20160317_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='myfield',
            field=models.CharField(max_length=256, choices=[(b'one', b'one')]),
        ),
    ]
