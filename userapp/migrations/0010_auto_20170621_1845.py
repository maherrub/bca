# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_auto_20170525_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='edited_on',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='zip_or_postal_code',
            new_name='postal_code',
        ),
        migrations.AddField(
            model_name='profilemanager',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profilemanager',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
