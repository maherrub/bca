# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_auto_20170621_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usercover',
            field=models.FileField(blank=True, null=True, upload_to='uploads/profile_pictures/', validators=[website.validators.validate_imagefile_extension]),
        ),
    ]
