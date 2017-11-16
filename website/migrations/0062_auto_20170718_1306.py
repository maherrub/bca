# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0061_teammember_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='member_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='member_title',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
