# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0063_auto_20170719_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map_box_size',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
