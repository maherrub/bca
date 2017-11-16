# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20170410_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-edited_on']},
        ),
        migrations.RemoveField(
            model_name='page',
            name='media_url',
        ),
    ]
