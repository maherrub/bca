# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_userprofile_ticket_manager_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpDeskManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hdmgr_functional_group', models.CharField(max_length=25, choices=[(b'Servicedesk', b'Servicedesk'), (b'IT', b'IT'), (b'Finance', b'Finance'), (b'HR', b'HR')])),
                ('hdmgr_functional_group_area', models.CharField(max_length=75)),
                ('hdmgr_ticket_manager_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.AutoField(serialize=False, primary_key=True)),
                ('ticket_category', models.CharField(max_length=50, choices=[(b'IT', b'IT'), (b'Others', b'Others')])),
                ('ticket_issue', models.CharField(max_length=100, null=True, blank=True)),
                ('ticket_priority', models.CharField(default='Normal', max_length=25, choices=[(b'Super Urgent', b'Super Urgent'), (b'Urgent', b'Urgent'), (b'Normal', b'Normal')])),
                ('ticket_status', models.CharField(default='Started', max_length=25, choices=[(b'Started', b'Started'), (b'In Progress', b'In Progress'), (b'Pending', b'Pending'), (b'Completed', b'Completed'), (b'Closed', b'Closed')])),
                ('ticket_description', models.TextField(blank=True)),
                ('ticket_screenshot', models.FileField(null=True, upload_to='helpdesk_snapshots/', blank=True)),
                ('consent_manager_name', models.CharField(max_length=20, null=True, blank=True)),
                ('consent_manager_approved', models.BooleanField(default=False)),
                ('ticket_edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('assigned_manager', models.ForeignKey(to='helpdesk.HelpDeskManager', blank=True)),
                ('consent_manager_key', models.ForeignKey(to='userapp.UserProfile', blank=True)),
                ('ticket_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-ticket_edited_on'],
            },
        ),
        migrations.CreateModel(
            name='TicketManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_manager_reply', models.TextField(blank=True)),
                ('ticket_manager_edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticket_manager_fg', models.ForeignKey(to='helpdesk.HelpDeskManager')),
                ('ticket_manager_name', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('ticket_manager_ticket', models.ForeignKey(to='helpdesk.Ticket')),
            ],
        ),
    ]
