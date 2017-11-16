# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0011_auto_20170622_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friendoffriend', models.CharField(max_length=150, null=True, blank=True)),
                ('frnd_options', models.CharField(max_length=25, choices=[(b'Friend Request', b'Friend Request'), (b'Accept Friend Request', b'Accept Friend Request'), (b'Unfriend', b'Unfriend')])),
                ('requested_date', models.DateTimeField(auto_now=True, null=True)),
                ('frndoffrnd_options', models.CharField(max_length=25, choices=[(b'Friend Request', b'Friend Request'), (b'Accept Friend Request', b'Accept Friend Request'), (b'Unfriend', b'Unfriend')])),
                ('accepted_date', models.DateTimeField(auto_now=True, null=True)),
                ('friend', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
