# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_userprofile_ticket_manager_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemanager',
            name='pm_functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sunday_service',
            field=models.CharField(default='English', max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
    ]
