# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20170502_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='card_type',
            field=models.CharField(default=b'Topic', max_length=25, choices=[(b'Topic', b'Topic'), (b'Link', b'Link')]),
        ),
    ]
