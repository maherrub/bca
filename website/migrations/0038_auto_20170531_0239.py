# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20170528_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='hgpi_link',
            new_name='button_link',
        ),
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='hgpi_link_button_name',
            new_name='button_name',
        ),
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='html_bgcolorcodes',
            new_name='html_bgcolorcode',
        ),
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='hgpi_image_main_text',
            new_name='main_text',
        ),
        migrations.RenameField(
            model_name='homegroupparallaximage',
            old_name='hgpi_image_secondary_text',
            new_name='secondary_text',
        ),
        migrations.RemoveField(
            model_name='homegroupparallaximage',
            name='hgpi_background',
        ),
        migrations.RemoveField(
            model_name='homegroupparallaximage',
            name='hgpi_name',
        ),
        migrations.RemoveField(
            model_name='homegroupparallaximage',
            name='png_desk_text',
        ),
        migrations.RemoveField(
            model_name='homegroupparallaximage',
            name='png_mobile_text',
        ),
    ]
