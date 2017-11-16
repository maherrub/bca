# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_auto_20170406_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='consent_manager_reason',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='consent_manager_approved',
            field=multiselectfield.db.fields.MultiSelectField(default='NAT', max_length=21, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected'), (b'NAT', b'NAT')]),
        ),
    ]
