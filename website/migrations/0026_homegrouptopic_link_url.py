# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_remove_homegrouptopic_cover_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='link_url',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
