# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_auto_20170601_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptext',
            name='page_id',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
