# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeGroupManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hgp_functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')])),
                ('hgp_manager_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HomeGroupParallaxImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')])),
                ('display_position', models.CharField(max_length=25, choices=[(b'IMAGE1', b'IMAGE1'), (b'IMAGE2', b'IMAGE2'), (b'IMAGE3', b'IMAGE3')])),
                ('hgpi_name', models.CharField(max_length=25, null=True, blank=True)),
                ('hgpi_background', models.FileField(null=True, upload_to=b'parallax_images/', blank=True)),
                ('hgpi_image_main_text', models.CharField(max_length=100, null=True, blank=True)),
                ('hgpi_image_secondary_text', models.CharField(max_length=200, null=True, blank=True)),
                ('hgpi_link_button_name', models.CharField(max_length=15, null=True, blank=True)),
                ('hgpi_link', models.CharField(max_length=50, null=True, blank=True)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('hgpi_owner', models.ForeignKey(to='website.HomeGroupManager')),
            ],
            options={
                'ordering': ['-edited_on'],
            },
        ),
        migrations.CreateModel(
            name='HomeGroupText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')])),
                ('display_position_text', models.CharField(max_length=25, choices=[(b'ROW1', b'ROW1'), (b'ROW3', b'ROW3'), (b'ROW5', b'ROW5'), (b'ROW7', b'ROW7'), (b'ROW9', b'ROW9')])),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('main_title_text', models.CharField(max_length=100, null=True, blank=True)),
                ('secondary_title_text', models.CharField(max_length=200, null=True, blank=True)),
                ('short_description_text', models.TextField(blank=True)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_owner', models.ForeignKey(to='website.HomeGroupManager')),
            ],
            options={
                'ordering': ['-edited_on'],
            },
        ),
        migrations.CreateModel(
            name='HomeGroupTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')])),
                ('display_position', models.CharField(max_length=25, choices=[(b'ROW2-COL1/3', b'ROW2-COL1/3'), (b'ROW2-COL2/3', b'ROW2-COL2/3'), (b'ROW2-COL3/3', b'ROW2-COL3/3'), (b'ROW4-COL1/4', b'ROW4-COL1/4'), (b'ROW4-COL2/4', b'ROW4-COL2/4'), (b'ROW4-COL3/4', b'ROW4-COL3/4'), (b'ROW4-COL4/4', b'ROW4-COL4/4'), (b'ROW6-COL1/3', b'ROW6-COL1/3'), (b'ROW6-COL2/3', b'ROW6-COL2/3'), (b'ROW6-COL3/3', b'ROW6-COL3/3')])),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('speaker_image', models.FileField(null=True, upload_to=b'speaker_images/', blank=True)),
                ('cover_image', models.FileField(null=True, upload_to=b'homegroup_images/', blank=True)),
                ('cover_video', models.FileField(null=True, upload_to=b'homegroup_videos/', blank=True)),
                ('main_title', models.CharField(max_length=25, null=True, blank=True)),
                ('secondary_title', models.CharField(max_length=75, null=True, blank=True)),
                ('day', models.CharField(max_length=15, null=True, blank=True)),
                ('date', models.CharField(max_length=15, null=True, blank=True)),
                ('time', models.CharField(max_length=15, null=True, blank=True)),
                ('venue', models.CharField(max_length=65, null=True, blank=True)),
                ('short_description', models.TextField(blank=True)),
                ('long_description', models.TextField(blank=True)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited_on'],
            },
        ),
    ]
