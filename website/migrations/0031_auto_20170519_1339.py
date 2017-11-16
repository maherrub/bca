# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20170519_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homegrouptopic',
            name='translatedtxtfile',
        ),
        migrations.AddField(
            model_name='extend',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/extends/', blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/extends/', blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/', blank=True),
        ),
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/parallax_images/', blank=True),
        ),
        migrations.AddField(
            model_name='homegrouptext',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/texts/', blank=True),
        ),
        migrations.AddField(
            model_name='homegrouptext',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/texts/', blank=True),
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/topics/', blank=True),
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/topics/', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/pages/', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/pages/', blank=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/teammembers/', blank=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/teammembers/', blank=True),
        ),
        migrations.AddField(
            model_name='teamname',
            name='translatedtxtfile1',
            field=models.FileField(null=True, upload_to=b'uploads/teamnames/', blank=True),
        ),
        migrations.AddField(
            model_name='teamname',
            name='translatedtxtfile2',
            field=models.FileField(null=True, upload_to=b'uploads/teamnames/', blank=True),
        ),
    ]
