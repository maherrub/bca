# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20170421_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extend',
            options={'ordering': ['display_section']},
        ),
        migrations.RemoveField(
            model_name='extend',
            name='display_order',
        ),
        migrations.AddField(
            model_name='extend',
            name='display_section',
            field=models.CharField(default=b'section1', max_length=10, choices=[(b'section1', b'section1'), (b'section2', b'section2'), (b'section3', b'section3'), (b'section4', b'section4'), (b'section5', b'section5'), (b'section6', b'section6'), (b'section7', b'section7'), (b'section8', b'section8'), (b'section9', b'section9')]),
        ),
    ]
