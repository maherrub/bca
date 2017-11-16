# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20170423_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamname',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teamname',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extend',
            name='layout',
            field=models.CharField(max_length=25, choices=[(b'parallax-style', b'parallax-style'), (b'picture-left-text-right', b'picture-left-text-right'), (b'text-left-picture-right', b'text-left-picture-right')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='layout',
            field=models.CharField(max_length=25, choices=[(b'parallax-style', b'parallax-style'), (b'picture-left-text-right', b'picture-left-text-right'), (b'text-left-picture-right', b'text-left-picture-right')]),
        ),
    ]
