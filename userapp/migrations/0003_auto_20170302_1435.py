# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20170220_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='community_services',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Community Lunch', b'Community Lunch'), (b'Tuition Centre', b'Tuition Centre'), (b'Prayer for the sick', b'Prayer for the sick'), (b'Monday Yum Cha', b'Monday Yum Cha'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='creative_media',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Actor', b'Actor'), (b'Actress', b'Actress'), (b'Camera', b'Camera'), (b'Director', b'Director'), (b'Screen Play', b'Screen Play'), (b'Costumes', b'Costumes'), (b'Music', b'Music'), (b'Editor', b'Editor'), (b'Choreographer', b'Choreographer'), (b'Mentor', b'Mentor'), (b'Production', b'Production'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='expertise',
            field=models.CharField(blank=True, max_length=15, choices=[(b'Admin', b'Admin'), (b'Management', b'Management'), (b'Music/Sound', b'Music/Sound'), (b'IT', b'IT'), (b'Designer', b'Designer'), (b'Programmer', b'Programmer'), (b'Volunteer', b'Volunteer'), (b'Planner', b'Planner'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='oikos',
            field=models.CharField(blank=True, max_length=75, choices=[(b'FAMILY OIKOS: BEDOK SOUTH AVENUE 3, Blk 161, #01-515, S(460161)', b'FAMILY OIKOS: BEDOK SOUTH AVENUE 3, Blk 161, #01-515, S(460161)'), (b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 1, S(461001)', b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 1, S(461001)'), (b'FAMILY OIKOS: CHAI CHEE ST Blk 51, #08-310, S(460051)', b'FAMILY OIKOS: CHAI CHEE ST Blk 51, #08-310, S(460051)'), (b'FAMILY OIKOS: CHAI CHEE ST Blk 54, #11-881, S(460054)', b'FAMILY OIKOS: CHAI CHEE ST Blk 54, #11-881, S(460054)'), (b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 19, #05-322 S(461019)', b'FAMILY OIKOS: CHAI CHEE ROAD, Blk 19, #05-322 S(461019)'), (b'FAMILY OIKOS: JALAN BANGSAWAN 67, S(457828)', b'FAMILY OIKOS: JALAN BANGSAWAN 67, S(457828)'), (b'FAMILY OIKOS: JALAN DAMAI, Blk 662, #13-135, S(410662)', b'FAMILY OIKOS: JALAN DAMAI, Blk 662, #13-135, S(410662)'), (b'FAMILY OIKOS: HAIG COURT, Blk 158 #14-04, S(438794)', b'FAMILY OIKOS: HAIG COURT, Blk 158 #14-04, S(438794)'), (b'FAMILY OIKOS: LORONG MELAYU, 78C, S(416985)', b'FAMILY OIKOS: LORONG MELAYU, 78C, S(416985)'), (b'FAMILY OIKOS: PASIR RIS ST 52 511, #15-131, S(510511) * 8:30pm', b'FAMILY OIKOS: PASIR RIS ST 52 511, #15-131, S(510511) * 8:30pm'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL Conference Room, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL Conference Room, 2nd Flr'), (b'FAMILY OIKOS: SENGKANG EAST WAY, Blk 122A, #08-53, S(541122)', b'FAMILY OIKOS: SENGKANG EAST WAY, Blk 122A, #08-53, S(541122)'), (b'FAMILY OIKOS: 1 SIMEI ST 4, #09-08, Simei Green S(529861)', b'FAMILY OIKOS: 1 SIMEI ST 4, #09-08, Simei Green S(529861)'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr (Friday, 10.30am)', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr (Friday, 10.30am)'), (b'FAMILY OIKOS: SUNSET WAY, Blk 135, #06-08, S(597158)', b'FAMILY OIKOS: SUNSET WAY, Blk 135, #06-08, S(597158)'), (b'FAMILY OIKOS: TAMPINES ST 24, Blk 230, #07-126, S(524230)', b'FAMILY OIKOS: TAMPINES ST 24, Blk 230, #07-126, S(524230)'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 5, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 5, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 1, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 1, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Classroom 2, 2nd Flr'), (b'FAMILY OIKOS: BETHESDA CATHEDRAL, Daniel Hall, 2nd Flr (Sunday, 12 pm)', b'FAMILY OIKOS: BETHESDA CATHEDRAL, Daniel Hall, 2nd Flr (Sunday, 12 pm)'), (b'YOUNG ADULTS: 10 AIDA STREET, S(459330)', b'YOUNG ADULTS: 10 AIDA STREET, S(459330)'), (b'YOUNG ADULTS: BETHESDA CATHEDRAL Joseph Hall, 4th Flr', b'YOUNG ADULTS: BETHESDA CATHEDRAL Joseph Hall, 4th Flr'), (b'YOUTH OIKOS: TERTIARY BEDOK NORTH AVENUE 1, Blk 552, #03-492, S(460552)', b'YOUTH OIKOS: TERTIARY BEDOK NORTH AVENUE 1, Blk 552, #03-492, S(460552)'), (b'YOUTH OIKOS: LOWER SEC GIRLS BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: LOWER SEC GIRLS BETHESDA CATHEDRAL (Sunday, 9:30 am)'), (b'YOUTH OIKOS: LOWER SEC BOYS BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: LOWER SEC BOYS BETHESDA CATHEDRAL (Sunday, 9:30 am)'), (b'YOUTH OIKOS: BEDOK GREEN SECONDARY SCHOOL (FRIDAY, 2PM)', b'YOUTH OIKOS: BEDOK GREEN SECONDARY SCHOOL (FRIDAY, 2PM)'), (b'YOUTH OIKOS: UPPER SECONDARY BETHESDA CATHEDRAL (Sunday, 9:30 am)', b'YOUTH OIKOS: UPPER SECONDARY BETHESDA CATHEDRAL (Sunday, 9:30 am)'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='outreach_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Make a difference day', b'Make a difference day'), (b'Health Screenings', b'Health Screenings'), (b'Financial peace courses', b'Financial peace courses'), (b'Basics of Christian Living', b'Basics of Christian Living'), (b'Pre-Marital Counselling', b'Pre-Marital Counselling'), (b'Homebound Ministry', b'Homebound Ministry'), (b'Computer Training', b'Computer Training'), (b'Music Classes', b'Music Classes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usher_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Traffic Warden', b'Traffic Warden'), (b'Greeting Usherer', b'Greeting Usherer'), (b'Holy Communion Serving', b'Holy Communion Serving'), (b'Offerings Usherer', b'Offerings Usherer'), (b'Altar Call Usherer', b'Altar Call Usherer'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='worship_ministry',
            field=models.CharField(blank=True, max_length=25, choices=[(b'Vocals', b'Vocals'), (b'Sound', b'Sound'), (b'Visuals', b'Visuals'), (b'Guitar', b'Guitar'), (b'Keys', b'Keys'), (b'Drums', b'Drums'), (b'Strings', b'Strings'), (b'No', b'No')]),
        ),
    ]
