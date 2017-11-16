# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0052_auto_20170707_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='aresourceitem',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
