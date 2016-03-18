# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0003_auto_20160317_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
    ]
