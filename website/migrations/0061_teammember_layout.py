# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0060_auto_20170718_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='layout',
            field=models.CharField(default=b'Standard', max_length=25, choices=[(b'Standard', b'Standard'), (b'Locale', b'Locale')]),
        ),
    ]
