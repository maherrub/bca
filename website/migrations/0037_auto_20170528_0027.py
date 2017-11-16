# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_auto_20170528_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='youtubeid',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
