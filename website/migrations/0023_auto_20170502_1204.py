# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_homegroupparallaximage_html_bgcolorcodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='landscape_background',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/landscape', blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='portrait_background',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/portrait', blank=True),
        ),
    ]
