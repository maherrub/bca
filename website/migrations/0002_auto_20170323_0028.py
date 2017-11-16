# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='hgpi_background',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/', blank=True),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='cover_image',
            field=models.FileField(null=True, upload_to=b'uploads/homegroup_images/', blank=True),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='cover_video',
            field=models.FileField(null=True, upload_to=b'uploads/homegroup_videos/', blank=True),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='speaker_image',
            field=models.FileField(null=True, upload_to=b'uploads/speaker_images/', blank=True),
        ),
    ]
