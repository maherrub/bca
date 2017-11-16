# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170324_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='hgpi_owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
