# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170323_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
