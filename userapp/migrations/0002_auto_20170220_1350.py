# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='community_services',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Community Lunch', b'Community Lunch'), (b'Tuition Centre', b'Tuition Centre'), (b'Prayer for the sick', b'Prayer for the sick'), (b'Monday Yum Cha', b'Monday Yum Cha')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='community_services_role',
            field=models.CharField(blank=True, max_length=25, choices=[(b'CS Volunteer', b'CS Volunteer'), (b'CS Volunteer-Leader', b'CS Volunteer-Leader'), (b'TC Volunteer', b'TC Volunteer'), (b'TC Volunteer-Leader', b'TC Volunteer-Leader'), (b'P4S Volunteer', b'P4S Volunteer'), (b'P4S Volunteer-Leader', b'P4S Volunteer-Leader'), (b'MYC Volunteer', b'MYC Volunteer'), (b'MYC Volunteer-Leader', b'MYC Volunteer-Leader')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='creative_media',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Actor', b'Actor'), (b'Actress', b'Actress'), (b'Camera', b'Camera'), (b'Director', b'Director'), (b'Screen Play', b'Screen Play'), (b'Costumes', b'Costumes'), (b'Music', b'Music'), (b'Editor', b'Editor'), (b'Choreographer', b'Choreographer'), (b'Mentor', b'Mentor'), (b'Production', b'Production')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='creative_media_role',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Actor', b'Actor'), (b'Actress', b'Actress'), (b'Camera', b'Camera'), (b'Director', b'Director'), (b'Asst. Director', b'Asst. Director'), (b'Screen Play Writer', b'Screen Play Writer'), (b'Costumes', b'Costumes'), (b'Music', b'Music'), (b'Editor', b'Editor'), (b'Choreographer', b'Choreographer'), (b'Mentor', b'Mentor'), (b'Production', b'Production')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='creative_media_team',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Team-1', b'Team-1'), (b'Team-2', b'Team-2'), (b'Team-3', b'Team-3'), (b'Team-4', b'Team-4'), (b'Team-5', b'Team-5'), (b'Team-6', b'Team-6')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='marital_status',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Single', b'Single'), (b'Married', b'Married'), (b'Separated', b'Separated')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='number_of_children',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='oikos',
            field=models.CharField(blank=True, max_length=75, choices=[(b'FAMILY OIKOS: BEDOK SOUTH AVENUE 3, Blk 161, #01-515, S(460161)', b'FAMILY OIKOS: BEDOK SOUTH AVENUE 3, Blk 161, #01-515, S(460161)'), (b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 1, S(461001)', b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 1, S(461001)'), (b'FAMILY OIKOS: CHAI CHEE ST Blk 51, #08-310, S(460051)', b'FAMILY OIKOS: CHAI CHEE ST Blk 51, #08-310, S(460051)'), (b'FAMILY OIKOS: CHAI CHEE ST Blk 54, #11-881, S(460054)', b'FAMILY OIKOS: CHAI CHEE ST Blk 54, #11-881, S(460054)'), (b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 19, #05-322 S(461019)', b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 19, #05-322 S(461019)'), (b'FAMILY OIKOS: JALAN BANGSAWAN 67, S(457828)', b'FAMILY OIKOS: JALAN BANGSAWAN 67, S(457828)'), (b'FAMILY OIKOS: JALAN DAMAI, Blk 662, #13-135, S(410662)', b'FAMILY OIKOS: JALAN DAMAI, Blk 662, #13-135, S(410662)'), (b'FAMILY OIKOS: HAIG COURT, Blk 158 #14-04, S(438794)', b'FAMILY OIKOS: HAIG COURT, Blk 158 #14-04, S(438794)'), (b'FAMILY OIKOS: LORONG MELAYU, 78C, S(416985)', b'FAMILY OIKOS: LORONG MELAYU, 78C, S(416985)'), (b'FAMILY OIKOS: PASIR RIS ST 52 511, #15-131, S(510511) * 8:30pm', b'FAMILY OIKOS: PASIR RIS ST 52 511, #15-131, S(510511) * 8:30pm'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL Conference Room, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL Conference Room, 2nd Flr'), (b'FAMILY OIKOS: SENGKANG EAST WAY, Blk 122A, #08-53, S(541122)', b'FAMILY OIKOS: SENGKANG EAST WAY, Blk 122A, #08-53, S(541122)'), (b'FAMILY OIKOS: 1 SIMEI ST 4, #09-08, Simei Green S(529861)', b'FAMILY OIKOS: 1 SIMEI ST 4, #09-08, Simei Green S(529861)'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr (Friday, 10.30am)', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr (Friday, 10.30am)'), (b'FAMILY OIKOS: SUNSET WAY, Blk 135, #06-08, S(597158)', b'FAMILY OIKOS: SUNSET WAY, Blk 135, #06-08, S(597158)'), (b'FAMILY OIKOS: TAMPINES ST 24, Blk 230, #07-126, S(524230)', b'FAMILY OIKOS: TAMPINES ST 24, Blk 230, #07-126, S(524230)'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 5, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 5, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 1, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 1, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Daniel Hall, 2nd Flr (Sunday, 12 pm)', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Daniel Hall, 2nd Flr (Sunday, 12 pm)'), (b'YOUNG ADULTS: 10 AIDA STREET, S(459330)', b'YOUNG ADULTS: 10 AIDA STREET, S(459330)'), (b'YOUNG ADULTS: BETHESDA CATHEDRAL Joseph Hall, 4th Flr', b'YOUNG ADULTS: BETHESDA CATHEDRAL Joseph Hall, 4th Flr'), (b'YOUTH OIKOS: TERTIARY BEDOK NORTH AVENUE 1, Blk 552, #03-492, S(460552)', b'YOUTH OIKOS: TERTIARY BEDOK NORTH AVENUE 1, Blk 552, #03-492, S(460552)'), (b'YOUTH OIKOS: LOWER SEC GIRLS BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: LOWER SEC GIRLS BETHESDA CATHEDRAL (Sunday, 9:30 am)'), (b'YOUTH OIKOS: LOWER SEC BOYS BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: LOWER SEC BOYS BETHESDA CATHEDRAL (Sunday, 9:30 am)'), (b'YOUTH OIKOS: BEDOK GREEN SECONDARY SCHOOL (FRIDAY, 2PM)', b'YOUTH OIKOS: BEDOK GREEN SECONDARY SCHOOL (FRIDAY, 2PM)'), (b'YOUTH OIKOS: UPPER SECONDARY BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: UPPER SECONDARY BETHESDA CATHEDRAL (Sunday, 9:30 am)')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='oikos_role',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Leader', b'Leader'), (b'Member', b'Member')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='outreach_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Make a difference day', b'Make a difference day'), (b'Health Screenings', b'Health Screenings'), (b'Financial peace courses', b'Financial peace courses'), (b'Basics of Christian Living', b'Basics of Christian Living'), (b'Pre-Marital Counselling', b'Pre-Marital Counselling'), (b'Homebound Ministry', b'Homebound Ministry'), (b'Computer Training', b'Computer Training'), (b'Music Classes', b'Music Classes')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='outreach_ministry_role',
            field=models.CharField(blank=True, max_length=25, choices=[(b'MADD -Outreach Champion', b'MADD -Outreach Champion'), (b'MADD -Outreach Leader', b'MADD -Outreach Leader'), (b'HS -Outreach Champion', b'HS -Outreach Champion'), (b'HS -Outreach Leader', b'HS -Outreach Leader'), (b'FPS -Outreach Champion', b'FPS -Outreach Champion'), (b'FPS -Outreach Leader', b'FPS -Outreach Leader'), (b'BOCL -Outreach Champion', b'BOCL -Outreach Champion'), (b'BOCL -Outreach Leader', b'BOCL -Outreach Leader'), (b'PMC -Outreach Champion', b'PMC -Outreach Champion'), (b'PMC -Outreach Leader', b'PMC -Outreach Leader'), (b'HM -Outreach Champion', b'HM -Outreach Champion'), (b'HM -Outreach Leader', b'HM -Outreach Leader'), (b'CT -Outreach Champion', b'CT -Outreach Champion'), (b'CT -Outreach Leader', b'CT -Outreach Leader'), (b'MC -Outreach Champion', b'MC -Outreach Champion'), (b'MC -Outreach Leader', b'MC -Outreach Leader')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='outreach_ministry_team',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Team-1', b'Team-1'), (b'Team-2', b'Team-2'), (b'Team-3', b'Team-3'), (b'Team-4', b'Team-4'), (b'Team-5', b'Team-5'), (b'Team-6', b'Team-6')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usher_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Traffic Warden', b'Traffic Warden'), (b'Greeting Usherer', b'Greeting Usherer'), (b'Holy Communion Serving', b'Holy Communion Serving'), (b'Offerings Usherer', b'Offerings Usherer'), (b'Altar Call Usherer', b'Altar Call Usherer')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usher_ministry_role',
            field=models.CharField(blank=True, max_length=40, choices=[(b'Traffic Warden-Volunteer', b'Traffic Warden-Volunteer'), (b'Traffic Warden-Volunteer-Leader', b'Traffic Warden-Volunteer-Leader'), (b'Greeting Usherer-Volunteer', b'Greeting Usherer-Volunteer'), (b'Greeting Usherer-Volunteer-Leader', b'Greeting Usherer-Volunteer-Leader'), (b'Holy Communion Serving-Usherer', b'Holy Communion Serving-Usherer'), (b'Holy Communion Serving-Usherer-Leader', b'Holy Communion Serving-Usherer-Leader'), (b'Offerings Usherer', b'Offerings Usherer'), (b'Offerings Usherer-Leader', b'Offerings Usherer-Leader'), (b'Altar Call Usherer', b'Altar Call Usherer'), (b'Altar Call Usherer-Leader', b'Altar Call Usherer-Leader')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='worship_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Vocals', b'Vocals'), (b'Sound', b'Sound'), (b'Visuals', b'Visuals'), (b'Guitar', b'Guitar'), (b'Keys', b'Keys'), (b'Drums', b'Drums'), (b'Strings', b'Strings')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='worship_ministry_role',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Worship Leader', b'Worship Leader'), (b'Male Vocal', b'Male Vocal'), (b'Female Vocal', b'Female Vocal'), (b'Lead Guitar', b'Lead Guitar'), (b'Bass Guitar', b'Bass Guitar'), (b'Rythm Guitar', b'Rythm Guitar'), (b'Sound System', b'Sound System'), (b'Visuals & Systems', b'Visuals & Systems'), (b'Keys', b'Keys'), (b'Strings', b'Strings'), (b'Drums', b'Drums'), (b'Inst. Maintenance', b'Inst. Maintenance')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='worship_ministry_team',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Team-1', b'Team-1'), (b'Team-2', b'Team-2'), (b'Team-3', b'Team-3'), (b'Team-4', b'Team-4'), (b'Team-5', b'Team-5'), (b'Team-6', b'Team-6')]),
        ),
    ]
