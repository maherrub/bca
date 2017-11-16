# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_auto_20170712_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='html_bgcolorcode',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
