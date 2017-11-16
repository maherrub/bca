# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0012_homegrouptopic_text_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hierarchy', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7')])),
                ('member_name', models.CharField(max_length=50)),
                ('member_picture', models.FileField(null=True, upload_to=b'uploads/pages/team/', blank=True)),
                ('member_title', models.CharField(max_length=50)),
                ('member_crux', models.TextField(blank=True)),
                ('member_displayposition', models.CharField(default=b'col1', max_length=4, choices=[(b'col1', b'col1'), (b'col2', b'col2')])),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['member_name'],
            },
        ),
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('team_pageid', models.ForeignKey(to='website.Page')),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='teamname_id',
            field=models.ForeignKey(to='website.TeamName'),
        ),
    ]
