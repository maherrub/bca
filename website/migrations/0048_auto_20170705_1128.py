# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0047_resource_functional_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
