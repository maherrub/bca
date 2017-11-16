# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salutation', models.CharField(default='Mr', max_length=4, choices=[(b'Mr', b'Mr'), (b'Mrs', b'Mrs'), (b'Ms', b'Ms'), (b'Mdm', b'Mdm'), (b'Dr', b'Dr'), (b'Past', b'Past'), (b'Evan', b'Evan'), (b'Prof', b'Prof'), (b'Mast', b'Mast')])),
                ('firstname', models.CharField(max_length=25, blank=True)),
                ('lastname', models.CharField(max_length=25, blank=True)),
                ('usercover', models.FileField(upload_to='profile_pictures/', blank=True)),
                ('usermobile', models.CharField(max_length=15, blank=True)),
                ('address_line1', models.CharField(max_length=30, blank=True)),
                ('address_line2', models.CharField(max_length=30, blank=True)),
                ('city_or_town', models.CharField(max_length=30, blank=True)),
                ('state_or_province', models.CharField(max_length=30, blank=True)),
                ('zip_or_postal_code', models.CharField(max_length=7, blank=True)),
                ('country', models.CharField(max_length=20, blank=True)),
                ('dob', models.DateField(default='1920-01-01', blank=True)),
                ('who_brought_you_here', models.CharField(max_length=40, blank=True)),
                ('whos_mobile_number', models.CharField(max_length=15, blank=True)),
                ('sunday_service', models.CharField(default='English', max_length=10, choices=[(b'English', b'English'), (b'Chinese', b'Chinese')])),
                ('expertise', models.CharField(blank=True, max_length=15, choices=[(b'Admin', b'Admin'), (b'Management', b'Management'), (b'Music/Sound', b'Music/Sound'), (b'IT', b'IT'), (b'Designer', b'Designer'), (b'Programmer', b'Programmer'), (b'Volunteer', b'Volunteer'), (b'Planner', b'Planner')])),
                ('membership', models.CharField(blank=True, max_length=10, choices=[(b'Member', b'Member'), (b'Regular', b'Regular'), (b'Visitor', b'Visitor')])),
                ('age_group', models.CharField(blank=True, max_length=10, choices=[(b'Senior', b'Senior'), (b'Adult', b'Adult'), (b'Youth', b'Youth'), (b'Junior', b'Junior')])),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
