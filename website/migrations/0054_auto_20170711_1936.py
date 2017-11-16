# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_auto_20170711_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aresourceitem',
            name='is_featured',
        ),
        migrations.AddField(
            model_name='aresource',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
