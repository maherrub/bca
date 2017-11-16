# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20170330_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ticket_manager_name',
            field=models.CharField(default='ticketmanager', max_length=20),
        ),
    ]
