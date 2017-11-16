# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_teammember_more_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='png_desk_text',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/pngdesktext', blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='png_mobile_text',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/pngmobiletext', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer_position',
            field=models.CharField(max_length=25, choices=[(b'col1', b'col1'), (b'col2', b'col2'), (b'col3', b'col3'), (b'col4', b'col4'), (b'Home', b'Home'), (b'VisitUs', b'VisitUs'), (b'JustUs', b'JustUs'), (b'WhatsOn', b'WhatsOn'), (b'OurFamily', b'OurFamily'), (b'EngageGrow', b'EngageGrow'), (b'Connect', b'Connect')]),
        ),
    ]
