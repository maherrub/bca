# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_auto_20170525_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='youtubeid',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='page',
            name='menu_position',
            field=models.CharField(max_length=50, choices=[(b'HOME', b'HOME'), (b'DISCOVER_BC', b'DISCOVER_BC'), (b'EXPERIENCE', b'EXPERIENCE'), (b'ENGAGE', b'ENGAGE'), (b'ENGAGE_OIKOS', b'ENGAGE_OIKOS'), (b'ENGAGE_FAMILY_OIKOS', b'ENGAGE_FAMILY_OIKOS'), (b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS', b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS'), (b'ENGAGE_WOMENS_MINISTRY', b'ENGAGE_WOMENS_MINISTRY'), (b'ENGAGE_WORSHIP_MINISTRY', b'ENGAGE_WORSHIP_MINISTRY'), (b'ENGAGE_YOUTH_AT_BC', b'ENGAGE_YOUTH_AT_BC'), (b'GROW', b'GROW'), (b'MANDARIN_MINISTRY', b'MANDARIN_MINISTRY'), (b'HOKKIEN_MINISTRY', b'HOKKIEN_MINISTRY'), (b'CANTONESE_MINISTRY', b'CANTONESE_MINISTRY'), (b'INDIAN_MINISTRY', b'INDIAN_MINISTRY'), (b'FILIPINO_MINISTRTY', b'FILIPINO_MINISTRTY'), (b'CONNECT', b'CONNECT'), (b'FOOTER_COL1', b'FOOTER_COL1'), (b'FOOTER_COL2', b'FOOTER_COL2'), (b'FOOTER_COL3', b'FOOTER_COL3'), (b'FOOTER_COL4', b'FOOTER_COL4')]),
        ),
    ]
