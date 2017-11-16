# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0015_auto_20170417_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layout', models.CharField(max_length=25, choices=[(b'picture-top-text-down', b'picture-top-text-down'), (b'picture-left-text-right', b'picture-left-text-right'), (b'text-left-picture-right', b'text-left-picture-right')])),
                ('display_order', models.CharField(max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9')])),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('main_title', models.CharField(max_length=100, null=True, blank=True)),
                ('high_title', models.CharField(max_length=100, null=True, blank=True)),
                ('high_title_color', models.CharField(max_length=20, choices=[(b'black-text', b'black-text'), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')])),
                ('extendmedia', models.FileField(null=True, upload_to=b'uploads/pages/extend', blank=True)),
                ('content', models.TextField(blank=True)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('extend_pageid', models.ForeignKey(to='website.Page')),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='font_style',
            field=models.CharField(default=b'font-brush', max_length=25, blank=True, choices=[(b'font-selima', b'font-selima'), (b'font-hensa', b'font-hensa'), (b'font-reis', b'font-reis'), (b'font-brush', b'font-brush'), (b'font-pompiere', b'font-pompiere'), (b'font-fredericka', b'font-fredericka'), (b'font-cinzel', b'font-cinzel'), (b'font-helvetica', b'font-helvetica'), (b'font-vibes', b'font-vibes')]),
        ),
    ]
