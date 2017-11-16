# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20170503_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegrouptopic',
            name='content_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
