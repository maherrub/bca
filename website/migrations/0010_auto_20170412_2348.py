# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170411_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegrouptopic',
            name='card_color',
            field=models.CharField(default=b'', max_length=25, choices=[(b'', b''), (b'danger-color', b'danger-color'), (b'danger-color-dark', b'danger-color-dark'), (b'warning-color', b'warning-color'), (b'warning-color-dark', b'warning-color-dark'), (b'success-color', b'success-color'), (b'success-color-dark', b'success-color-dark'), (b'info-color', b'info-color'), (b'info-color-dark', b'info-color-dark'), (b'default-color', b'default-color'), (b'default-color-dark', b'default-color-dark'), (b'primary-color', b'primary-color'), (b'primary-color-dark', b'primary-color-dark'), (b'secondary-color', b'secondary-color'), (b'secondary-color-dark', b'secondary-color-dark'), (b'elegant-color', b'elegant-color'), (b'elegant-color-dark', b'elegant-color-dark'), (b'stylish-color', b'stylish-color'), (b'stylish-color-dark', b'stylish-color-dark'), (b'unique-color', b'unique-color'), (b'unique-color-dark', b'unique-color-dark'), (b'special-color', b'special-color'), (b'special-color-dark', b'special-color-dark'), (b'red lighten-5', b'red lighten-5'), (b'red lighten-3', b'red lighten-3'), (b'red', b'red'), (b'red darken-2', b'red darken-2'), (b'red darken-4', b'red darken-4'), (b'red accent-4', b'red accent-4'), (b'pink lighten-5', b'pink lighten-5'), (b'pink lighten-2', b'pink lighten-2'), (b'pink', b' pink'), (b'pink darken-3', b'pink darken-3'), (b'pink darken-4', b'pink darken-4'), (b'purple lighten-5', b'purple lighten-5'), (b'purple lighten-2', b'purple lighten-2'), (b'purple', b'purple'), (b'purple darken-2', b'purple darken-2'), (b'purple darken-4', b'purple darken-4'), (b'purple accent-5', b'purple accent-5'), (b'indigo accent-1', b'indigo accent-1'), (b'blue lighten-5', b'blue lighten-5'), (b'blue accent-1', b' blue accent-1'), (b'light-blue lighten-5', b'light-blue lighten-5'), (b'light-blue lighten-4', b'light-blue lighten-4'), (b'light-blue', b'light-blue'), (b'light-blue darken-4', b'light-blue darken-4'), (b'light-blue accent-2', b'light-blue accent-2'), (b'light-blue accent-4', b'light-blue accent-4'), (b'cyan lighten-4', b'cyan lighten-4'), (b'cyan', b'cyan'), (b'cyan darken-2', b'cyan darken-2'), (b'cyan darken-4', b'cyan darken-4'), (b'cyan accent-1', b'cyan accent-1'), (b'teal lighten-5', b'teal lighten-5'), (b'teal accent-1', b'teal accent-1'), (b'green lighten-5', b'green lighten-5'), (b'green lighten-3', b'green lighten-3'), (b'green accent-2', b'green accent-2'), (b'green accent-3', b'green accent-3'), (b'lime darken-4', b'lime darken-4'), (b'lime accent-1', b'lime accent-1'), (b'lime accent-2', b'lime accent-2'), (b'yellow lighten-4', b'yellow lighten-4'), (b'amber darken-4', b'amber darken-4'), (b'amber accent-3', b'amber accent-3'), (b'orange', b'orange'), (b'orange darken-4', b'orange darken-4'), (b'rgba-green-strong', b'rgba-green-strong'), (b'rgba-brown-strong', b'rgba-brown-strong'), (b'rgba-black-strong', b'rgba-black-strong')]),
        ),
        migrations.AddField(
            model_name='homegrouptopic',
            name='card_style',
            field=models.CharField(default=b'', max_length=25, choices=[(b'', b''), (b'card-cascade', b'card-cascade'), (b'card-cascade narrower', b'card-cascade narrower'), (b'card-cascade wider', b'card-cascade wider')]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='display_position',
            field=models.CharField(max_length=25, choices=[(b'ROW2-COL1/4', b'ROW2-COL1/4'), (b'ROW2-COL2/4', b'ROW2-COL2/4'), (b'ROW2-COL3/4', b'ROW2-COL3/4'), (b'ROW2-COL4/4', b'ROW2-COL4/4'), (b'ROW4-COL1/4', b'ROW4-COL1/4'), (b'ROW4-COL2/4', b'ROW4-COL2/4'), (b'ROW4-COL3/4', b'ROW4-COL3/4'), (b'ROW4-COL4/4', b'ROW4-COL4/4'), (b'ROW6-COL1/4', b'ROW6-COL1/4'), (b'ROW6-COL2/4', b'ROW6-COL2/4'), (b'ROW6-COL3/4', b'ROW6-COL3/4'), (b'ROW6-COL4/4', b'ROW6-COL4/4')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='high_title_color',
            field=models.CharField(max_length=20, choices=[(b'', b''), (b'white-text', b'white-text'), (b'red-text', b'red-text'), (b'pink-text', b'pink-text'), (b'purple-text', b'purple-text'), (b'deep-purple-text', b'deep-purple-text'), (b'indigo-text', b'indigo-text'), (b'blue-text', b'blue-text'), (b'light-blue-text', b'light-blue-text'), (b'cyan-text', b'cyan-text'), (b'teal-text', b'teal-text'), (b'green-text', b'green-text'), (b'light-green-text', b'light-green-text'), (b'lime-text', b'lime-text'), (b'yellow-text', b'yellow-text'), (b'amber-text', b'amber-text'), (b'orange-text', b'orange-text'), (b'deep-orange-text', b'deep-orange-text'), (b'brown-text', b'brown-text'), (b'grey-text', b'grey-text'), (b'blue-grey-text', b'blue-grey-text')]),
        ),
    ]
