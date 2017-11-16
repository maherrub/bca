# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20170423_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='layout',
        ),
    ]
