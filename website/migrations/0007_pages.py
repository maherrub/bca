# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_homegrouptopic_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino')])),
                ('layout', models.CharField(max_length=25, choices=[(b'picture-top-text-down', b'picture-top-text-down'), (b'picture-left-text-right', b'picture-left-text-right'), (b'text-left-picture-right', b'text-left-picture-right')])),
                ('footer_position', models.CharField(max_length=25, choices=[(b'col1', b'col1'), (b'col2', b'col2'), (b'col3', b'col3'), (b'col4', b'col4')])),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('main_title', models.CharField(max_length=100, null=True, blank=True)),
                ('high_title', models.CharField(max_length=100, null=True, blank=True)),
                ('high_title_color', models.CharField(max_length=20, choices=[(b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')])),
                ('covermedia', models.FileField(null=True, upload_to=b'uploads/pages/', blank=True)),
                ('media_url', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('content', models.TextField(blank=True)),
                ('left_btnname', models.CharField(max_length=25, null=True, blank=True)),
                ('left_btnlink', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('right_btnname', models.CharField(max_length=25, null=True, blank=True)),
                ('right_btnlink', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('footer_linkname', models.CharField(max_length=25, null=True, blank=True)),
                ('footer_btnlink', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
