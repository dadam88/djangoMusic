# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160317_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin_name', models.CharField(unique=True, max_length=128, verbose_name='admin full name')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Admin Info',
            },
        ),
        migrations.CreateModel(
            name='Admin_Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin', models.ForeignKey(verbose_name='Administrator', to='polls.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admins', models.ManyToManyField(to='polls.Admin', verbose_name='Administrators', through='polls.Admin_Payment')),
                ('client', models.ForeignKey(verbose_name='Client', to='polls.Client')),
            ],
        ),
        migrations.AddField(
            model_name='admin_payment',
            name='project',
            field=models.ForeignKey(verbose_name='project', to='polls.Project'),
        ),
    ]
