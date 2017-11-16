# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20170707_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='version',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
