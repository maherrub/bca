# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0066_auto_20170720_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='extend',
            name='map1_box_size',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='map1_coordinate',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='map1_link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='extend',
            name='map1_tooltip',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='map2_box_size',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='map2_coordinate',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extend',
            name='map2_link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='extend',
            name='map2_tooltip',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extend',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center'), (b'50% 5%', b'50% 5%'), (b'50% 10%', b'50% 10%'), (b'50% 15%', b'50% 15%'), (b'50% 20%', b'50% 20%'), (b'50% 25%', b'50% 25%'), (b'50% 30%', b'50% 30%'), (b'50% 35%', b'50% 35%'), (b'50% 40%', b'50% 40%'), (b'50% 45%', b'50% 45%'), (b'50% 50%', b'50% 50%'), (b'50% 55%', b'50% 55%'), (b'50% 60%', b'50% 60%'), (b'50% 65%', b'50% 65%'), (b'50% 70%', b'50% 70%'), (b'50% 75%', b'50% 75%'), (b'50% 80%', b'50% 80%'), (b'50% 85%', b'50% 85%'), (b'50% 90%', b'50% 90%'), (b'50% 95%', b'50% 95%')]),
        ),
        migrations.AlterField(
            model_name='extend',
            name='layout',
            field=models.CharField(default=b'parallax-style', max_length=25, choices=[(b'parallax-style', b'parallax-style'), (b'picture-left-text-right', b'picture-left-text-right'), (b'text-left-picture-right', b'text-left-picture-right'), (b'plx-imgmap-link', b'plx-imgmap-link'), (b'plx-imgmap-tooltip', b'plx-imgmap-tooltip'), (b'plx-imgmap-tooltip-link', b'plx-imgmap-tooltip-link'), (b'plx-moveable-txtbox', b'plx-moveable-txtbox'), (b'plx-moveable-txtbox-link', b'plx-moveable-txtbox-link')]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center'), (b'50% 5%', b'50% 5%'), (b'50% 10%', b'50% 10%'), (b'50% 15%', b'50% 15%'), (b'50% 20%', b'50% 20%'), (b'50% 25%', b'50% 25%'), (b'50% 30%', b'50% 30%'), (b'50% 35%', b'50% 35%'), (b'50% 40%', b'50% 40%'), (b'50% 45%', b'50% 45%'), (b'50% 50%', b'50% 50%'), (b'50% 55%', b'50% 55%'), (b'50% 60%', b'50% 60%'), (b'50% 65%', b'50% 65%'), (b'50% 70%', b'50% 70%'), (b'50% 75%', b'50% 75%'), (b'50% 80%', b'50% 80%'), (b'50% 85%', b'50% 85%'), (b'50% 90%', b'50% 90%'), (b'50% 95%', b'50% 95%')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center'), (b'50% 5%', b'50% 5%'), (b'50% 10%', b'50% 10%'), (b'50% 15%', b'50% 15%'), (b'50% 20%', b'50% 20%'), (b'50% 25%', b'50% 25%'), (b'50% 30%', b'50% 30%'), (b'50% 35%', b'50% 35%'), (b'50% 40%', b'50% 40%'), (b'50% 45%', b'50% 45%'), (b'50% 50%', b'50% 50%'), (b'50% 55%', b'50% 55%'), (b'50% 60%', b'50% 60%'), (b'50% 65%', b'50% 65%'), (b'50% 70%', b'50% 70%'), (b'50% 75%', b'50% 75%'), (b'50% 80%', b'50% 80%'), (b'50% 85%', b'50% 85%'), (b'50% 90%', b'50% 90%'), (b'50% 95%', b'50% 95%')]),
        ),
    ]
