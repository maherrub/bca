# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import website.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0048_auto_20170705_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='aResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('functional_group', models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')])),
                ('cover', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/cover/', validators=[website.validators.validate_imagefile_extension])),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('title_locale', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/title/', validators=[website.validators.validate_transfile_extension])),
                ('author', models.CharField(max_length=25, null=True, blank=True)),
                ('author_locale', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/author/', validators=[website.validators.validate_transfile_extension])),
                ('language', models.CharField(default=b'English', max_length=25, choices=[(b'English', b'English'), (b'Mandarin', b'Mandarin'), (b'Cantonese', b'Cantonese'), (b'Hokkien', b'Hokkien'), (b'Tamil', b'Tamil'), (b'Telugu', b'Telugu'), (b'Malayalam', b'Malayalam'), (b'Tagalog', b'Tagalog')])),
                ('search_keywords_file', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/tags/', validators=[website.validators.validate_transfile_extension])),
                ('genre', models.CharField(default=b'Sermon', max_length=25, choices=[(b'Article', b'Article'), (b'Sermon', b'Sermon'), (b'Worship', b'Worship'), (b'Music Album', b'Music Album'), (b'Photo Album', b'Photo Album'), (b'Roster', b'Roster'), (b'Form', b'Form'), (b'Book', b'Book')])),
                ('is_favorite', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='resource',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
