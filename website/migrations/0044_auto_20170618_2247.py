# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_auto_20170618_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='layout',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='card_style',
            field=models.CharField(blank=True, max_length=25, choices=[(b'', b'standard'), (b'card-cascade', b'card-cascade'), (b'card-cascade narrower', b'card-cascade narrower'), (b'card-cascade wider', b'card-cascade wider')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='card_type',
            field=models.CharField(default=b'Topic', max_length=25, choices=[(b'Topic', b'Topic'), (b'Text', b'Text'), (b'Link', b'Link')]),
        ),
    ]
