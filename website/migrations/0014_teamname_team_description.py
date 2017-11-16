# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20170415_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamname',
            name='team_description',
            field=models.TextField(blank=True),
        ),
    ]
