# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_auto_20170407_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='consent_manager_approved',
        ),
        migrations.AddField(
            model_name='ticket',
            name='consent_manager_signed',
            field=models.CharField(default='', max_length=25, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
    ]
