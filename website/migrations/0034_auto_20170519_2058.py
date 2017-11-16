# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20170519_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupmanager',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='homegroupmanager',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
