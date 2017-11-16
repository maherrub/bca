# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0002_auto_20160607_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=140, null=True, verbose_name='Subject', blank=True),
        ),
    ]
