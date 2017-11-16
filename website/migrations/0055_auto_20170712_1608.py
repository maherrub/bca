# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0054_auto_20170711_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='layout',
            field=models.CharField(default=b'BGPF', max_length=25, choices=[(b'BGVI', b'BackgroundVideo'), (b'BGPF', b'BackgroundPictureFull'), (b'SBAN', b'StretchedBanner100'), (b'ABAN', b'AsIsBannerX100'), (b'RBAN', b'AsIsBannerRaisedX100'), (b'CBAN', b'BgColoredBanner100')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='layout',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'4', b'4'), (b'5', b'Five')]),
        ),
    ]
