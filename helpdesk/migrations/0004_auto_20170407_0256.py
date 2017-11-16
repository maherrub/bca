# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_auto_20170407_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='consent_manager_approved',
            field=models.CharField(default='', max_length=25, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected'), (b'NAT', b'NAT')]),
        ),
    ]
