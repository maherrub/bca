# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20170519_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
