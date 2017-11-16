# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170324_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegrouptext',
            name='content_owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
