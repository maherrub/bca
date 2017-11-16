# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170325_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='file_type',
            field=models.CharField(default='Image', max_length=25, choices=[(b'Image', b'Image'), (b'Video', b'Video')]),
            preserve_default=False,
        ),
    ]
