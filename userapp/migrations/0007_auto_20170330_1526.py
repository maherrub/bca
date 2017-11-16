# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_profilemanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sunday_service',
            field=models.CharField(default='English', max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')]),
        ),
    ]
