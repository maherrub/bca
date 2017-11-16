# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0059_extend_focus'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegroupparallaximage',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center')]),
        ),
        migrations.AddField(
            model_name='page',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center')]),
        ),
        migrations.AddField(
            model_name='teammember',
            name='form_locale',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/teammembers/', validators=[website.validators.validate_transfile_extension]),
        ),
        migrations.AlterField(
            model_name='extend',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom'), (b'top center', b'top center'), (b'bottom center', b'bottom center')]),
        ),
    ]
