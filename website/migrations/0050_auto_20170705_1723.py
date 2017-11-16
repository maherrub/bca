# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0049_auto_20170705_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='aResourceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=50, null=True, blank=True)),
                ('item_name_locale', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/item_name/', validators=[website.validators.validate_transfile_extension])),
                ('file_type', models.CharField(max_length=25, choices=[(b'ppt', b'ppt'), (b'pptx', b'pptx'), (b'pdf', b'pdf'), (b'mp3', b'mp3'), (b'mp4', b'mp4')])),
                ('resource_item', models.FileField(blank=True, null=True, upload_to=b'uploads/resources/item/', validators=[website.validators.validate_resourceitem_extension])),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='aresource',
            name='description',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/resources/description/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AddField(
            model_name='aresourceitem',
            name='resource_id',
            field=models.ForeignKey(to='website.aResource'),
        ),
    ]
