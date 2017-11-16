# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_auto_20170713_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='layout_text',
            field=models.CharField(default=b'TLST', max_length=25, choices=[(b'PARA', b'Paragraph'), (b'PARAi', b'Paragraph italic'), (b'TLST', b'First ln Header List'), (b'TLSTv', b'First ln Header List Variant'), (b'SLST', b'Simple List'), (b'SLSTv', b'Simple List Variant'), (b'SLSTc', b'Simple List Contained')]),
        ),
    ]
