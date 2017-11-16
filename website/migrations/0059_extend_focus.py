# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0058_auto_20170714_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='extend',
            name='focus',
            field=models.CharField(default=b'top center', max_length=25, choices=[(b'left top', b'left top'), (b'left center', b'left center'), (b'left bottom', b'left bottom'), (b'right top', b'right top'), (b'right center', b'right center'), (b'right bottom', b'right bottom'), (b'center top', b'center top'), (b'center center', b'center center'), (b'center bottom', b'center bottom')]),
        ),
    ]
