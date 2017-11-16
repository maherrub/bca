# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0065_auto_20170720_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='layout',
            field=models.CharField(default=b'LAON', max_length=25, choices=[(b'NOIM', b'No image'), (b'LAON', b'Landscape only'), (b'LAPO', b'Landscape and portrait'), (b'LAONim', b'Landscape with image map to link'), (b'LAONimt', b'Landscape with image map and tooltip'), (b'LAONimtl', b'Landscape with image map,tooltip with link'), (b'LAONmtb', b'Landscape with moveable textbox'), (b'LAONmtbl', b'Landscape with moveable textbox with link')]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='map1_tooltip',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='map2_tooltip',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
