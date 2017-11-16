# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20170302_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='manager_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='manager_type',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Legal Manager', b'Legal Manager'), (b'Leader', b'Leader')]),
        ),
    ]
