# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0062_auto_20170718_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='layout',
            field=models.CharField(default=b'LAON', max_length=25, choices=[(b'NOIM', b'No image'), (b'LAON', b'Landscape only'), (b'LAPO', b'Landscape and portrait'), (b'LAONim', b'Landscape with image map'), (b'LAONimt', b'Landscape with image map and tooltip'), (b'LAPOim', b'Landscape and Portrait with image map'), (b'LAPOimt', b'Landscape and Portrait with image map and tooltip')]),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map1_coordinate',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map1_link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map1_tooltip',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map2_coordinate',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map2_link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='map2_tooltip',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='menu_position',
            field=models.CharField(max_length=50, choices=[(b'HOME', b'HOME'), (b'DISCOVER_BC', b'DISCOVER_BC'), (b'EXPERIENCE', b'EXPERIENCE'), (b'ENGAGE', b'ENGAGE'), (b'ENGAGE_OIKOS', b'ENGAGE_OIKOS'), (b'ENGAGE_FAMILY_OIKOS', b'ENGAGE_FAMILY_OIKOS'), (b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS', b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS'), (b'ENGAGE_WOMENS_MINISTRY', b'ENGAGE_WOMENS_MINISTRY'), (b'ENGAGE_WORSHIP_MINISTRY', b'ENGAGE_WORSHIP_MINISTRY'), (b'ENGAGE_YOUTH_AT_BC', b'ENGAGE_YOUTH_AT_BC'), (b'ENGAGE_KIDS_CONNECT', b'ENGAGE_KIDS_CONNECT'), (b'ENGAGE_EVANGELISM', b'ENGAGE_EVANGELISM'), (b'ENGAGE_PRAYER_MINISTRY', b'ENGAGE_PRAYER_MINISTRY'), (b'ENGAGE_SOCIAL_CONCERNS', b'ENGAGE_SOCIAL_CONCERNS'), (b'ENGAGE_TUITION_CENTRE', b'ENGAGE_TUITION_CENTRE'), (b'ENGAGE_USHER_MINISTRY', b'ENGAGE_USHER_MINISTRY'), (b'GROW', b'GROW'), (b'MANDARIN_MINISTRY', b'MANDARIN_MINISTRY'), (b'HOKKIEN_MINISTRY', b'HOKKIEN_MINISTRY'), (b'CANTONESE_MINISTRY', b'CANTONESE_MINISTRY'), (b'INDIAN_MINISTRY', b'INDIAN_MINISTRY'), (b'FILIPINO_MINISTRTY', b'FILIPINO_MINISTRTY'), (b'CONNECT', b'CONNECT'), (b'FOOTER_COL1', b'FOOTER_COL1'), (b'FOOTER_COL2', b'FOOTER_COL2'), (b'FOOTER_COL3', b'FOOTER_COL3'), (b'FOOTER_COL4', b'FOOTER_COL4')]),
        ),
    ]
