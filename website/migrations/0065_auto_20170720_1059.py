# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0064_homegroupparallaximage_map_box_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='map_box_size',
            new_name='map1_box_size',
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map2_box_size',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
