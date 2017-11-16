# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_homegrouptopic_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='speaker_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='card_style',
            field=models.CharField(blank=True, max_length=25, choices=[(b'standard', b''), (b'card-cascade', b'card-cascade'), (b'card-cascade narrower', b'card-cascade narrower'), (b'card-cascade wider', b'card-cascade wider')]),
        ),
    ]
