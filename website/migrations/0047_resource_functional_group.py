# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0046_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='functional_group',
            field=models.CharField(default='English', max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
            preserve_default=False,
        ),
    ]
