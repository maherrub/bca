# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20170531_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='page_id',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extend',
            name='extendmedia',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/pages/extend', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='extend',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/extends/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='extend',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/extends/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='landscape_background',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/parallax_images/landscape', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='portrait_background',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/parallax_images/portrait', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/parallax_images/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/parallax_images/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/homegroup_images/', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='speaker_image',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/speaker_images/', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/topics/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/topics/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='page',
            name='covermedia',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/pages/', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='page',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/pages/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='page',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/pages/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='member_picture',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/pages/team/', validators=[website.validators.validate_imagefile_extension]),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/teammembers/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/teammembers/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='teamname',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/teamnames/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='teamname',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/teamnames/', validators=[website.validators.validate_transfile_extension]),
        ),
    ]
