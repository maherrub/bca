# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import website.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20170519_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='footer_btnlink',
            new_name='menu_link',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='footer_linkname',
            new_name='menu_name',
        ),
        migrations.RemoveField(
            model_name='page',
            name='footer_position',
        ),
        migrations.AddField(
            model_name='page',
            name='menu_position',
            field=models.CharField(default=datetime.datetime(2017, 5, 25, 7, 53, 26, 138000, tzinfo=utc), max_length=50, choices=[(b'FOOTER_COL1', b'FOOTER_COL1'), (b'FOOTER_COL2', b'FOOTER_COL2'), (b'FOOTER_COL3', b'FOOTER_COL3'), (b'FOOTER_COL4', b'FOOTER_COL4'), (b'HOME', b'HOME'), (b'DISCOVER_BC', b'DISCOVER_BC'), (b'EXPERIENCE', b'EXPERIENCE'), (b'ENGAGE', b'ENGAGE'), (b'ENGAGE_FAMILY_OIKOS', b'ENGAGE_FAMILY_OIKOS'), (b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS', b'ENGAGE_YOUTH_YOUNG_ADUILTS_OIKOS'), (b'GROW', b'GROW'), (b'MANDARIN_MINISTRY', b'MANDARIN_MINISTRY'), (b'HOKKIEN_MINISTRY', b'HOKKIEN_MINISTRY'), (b'CANTONESE_MINISTRY', b'CANTONESE_MINISTRY'), (b'INDIAN_MINISTRY', b'INDIAN_MINISTRY'), (b'FILIPINO_MINISTRTY', b'FILIPINO_MINISTRTY'), (b'CONNECT', b'CONNECT')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homegroupmanager',
            name='hgp_functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
        migrations.AlterField(
            model_name='homegroupparallaximage',
            name='functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
        migrations.AlterField(
            model_name='homegrouptext',
            name='functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
        migrations.AlterField(
            model_name='homegrouptext',
            name='translatedtxtfile1',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/texts/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptext',
            name='translatedtxtfile2',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/texts/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='homegrouptopic',
            name='functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='functional_group',
            field=models.CharField(max_length=25, choices=[(b'English', b'English'), (b'Chinese', b'Chinese'), (b'Hokkien', b'Hokkien'), (b'Cantonese', b'Cantonese'), (b'Indian', b'Indian'), (b'Filipino', b'Filipino'), (b'All', b'All')]),
        ),
    ]
