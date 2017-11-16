# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import website.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20170705_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=25, null=True, blank=True)),
                ('version', models.CharField(max_length=5, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('developed_by', models.CharField(max_length=25, null=True, blank=True)),
                ('released_by', models.CharField(max_length=25, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='aresourceitem',
            name='resource_item',
            field=models.FileField(blank=True, null=True, upload_to=b'downloads/resources/item/', validators=[website.validators.validate_resourceitem_extension]),
        ),
    ]
