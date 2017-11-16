# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20170428_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='html_bgcolorcodes',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
