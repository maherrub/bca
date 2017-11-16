# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_homegrouptopic_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homegrouptopic',
            name='cover_video',
        ),
    ]
