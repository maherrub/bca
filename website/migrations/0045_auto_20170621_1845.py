# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0044_auto_20170618_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extend',
            name='high_title_color',
            field=models.CharField(max_length=20, choices=[(b'black-text', b'black-text'), (b'grey-text', b'grey-text'), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='font_color',
            field=models.CharField(default=b'black-text', max_length=25, blank=True, choices=[(b'black-text', b'black-text'), (b'grey-text', b'grey-text'), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='layout',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'4', b'4')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='text_color',
            field=models.CharField(blank=True, max_length=25, choices=[(b'black-text', b'black-text'), (b'grey-text', b'grey-text'), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='high_title_color',
            field=models.CharField(max_length=20, choices=[(b'black-text', b'black-text'), (b'grey-text', b'grey-text'), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')]),
        ),
    ]
