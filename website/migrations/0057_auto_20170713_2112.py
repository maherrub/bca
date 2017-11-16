# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0056_page_html_bgcolorcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='layout_text',
            field=models.CharField(default=b'PARA', max_length=25, choices=[(b'PARA', b'Paragraph'), (b'PARAi', b'Paragraph italic'), (b'TLST', b'12 First ln Header List'), (b'TLSTi', b'12 First ln Header List italic'), (b'SLST', b'12 Simple List'), (b'SLSTi', b'12 Simple List italic')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='layout',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'4', b'4')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='layout',
            field=models.CharField(default=b'BGPF', max_length=25, choices=[(b'BGVI', b'BackgroundVideo'), (b'BGPF', b'BackgroundPictureFull'), (b'SBAN', b'StretchedBanner100'), (b'SBANi', b'StretchedBanner100i'), (b'ABAN', b'AsIsBannerX100'), (b'ABANi', b'AsIsBannerX100i'), (b'RBAN', b'AsIsBannerRaisedX100'), (b'RBANi', b'AsIsBannerRaisedX100i'), (b'CBAN', b'BgColoredBanner100'), (b'CBANi', b'BgColoredBanner100i')]),
        ),
    ]
