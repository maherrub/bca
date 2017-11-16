# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20170407_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='first_create_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 8, 7, 15, 57, 773000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='last_modified_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 8, 7, 16, 21, 390000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticketmanager',
            name='first_create_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 8, 7, 16, 36, 670000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticketmanager',
            name='last_modified_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 8, 7, 16, 53, 348000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='consent_manager_signed',
            field=models.CharField(default='', max_length=25, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected'), (b'', b'')]),
        ),
    ]
