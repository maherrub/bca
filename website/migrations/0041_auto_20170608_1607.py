# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_homegrouptext_page_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homegrouptopic',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='homegrouptopic',
            name='link_url',
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='page_id',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='youtubeid',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
