# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_manager',
            field=models.ForeignKey(default=1, to='helpdesk.HelpDeskManager'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='consent_manager_key',
            field=models.ForeignKey(default=1, to='userapp.UserProfile'),
        ),
    ]
