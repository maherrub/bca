# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0003_auto_20170622_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(default=datetime.datetime(2017, 6, 22, 16, 15, 36, 342000, tzinfo=utc), max_length=140, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
