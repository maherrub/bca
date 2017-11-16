from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


#Local apps imports
from website.choices import *
from website.validators import *
from userapp.choices import *


#definitions
app_name = 'userapp'

#models.

class UserProfile(models.Model):
       
    user = models.ForeignKey(User, default=1)
    salutation = models.CharField(max_length=4, choices=SALUTATION_LIST, default='Mr')  
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    usercover = models.FileField(upload_to='uploads/profile_pictures/', validators=[validate_imagefile_extension], null=True, blank=True)
    usermobile = models.CharField(max_length=15, blank=True)
    address_line1 = models.CharField(max_length=30, blank=True)
    address_line2 = models.CharField(max_length=30, blank=True)
    city_or_town = models.CharField(max_length=30, blank=True)
    state_or_province = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=7, blank=True)
    country = models.CharField(max_length=20, blank=True)
    dob = models.DateField(default='1920-01-01', blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_LIST, blank=True)
    number_of_children = models.IntegerField(choices=CHILDREN_LIST,null=True, blank=True)
    who_brought_you_here = models.CharField(max_length=40, blank=True)
    whos_mobile_number = models.CharField(max_length=15, blank=True)
    sunday_service = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST, default='English')
    expertise = models.CharField(max_length=15, choices=EXPERTISE_LIST, blank=True)
    membership = models.CharField(max_length=10, choices=MEMBERSHIP_LIST, blank=True)
    is_leader = models.BooleanField(default=False,)
    manager_name = models.CharField(max_length=20, blank=True)
    ticket_manager_name = models.CharField(max_length=20, default='ticketmanager')
    manager_type = models.CharField(max_length=20, choices=MANAGER_TYPE_LIST, blank=True)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_LIST, blank=True)
    oikos = models.CharField(max_length=75, choices=OIKOS_LIST, blank=True)
    oikos_role = models.CharField(max_length=10, choices=OIKOS_ROLE_LIST, blank=True)
    community_services = models.CharField(max_length=25, choices=COMMUNITY_SERVICES_LIST, blank=True)
    community_services_role = models.CharField(max_length=25, choices=COMMUNITY_SERVICES_ROLE_LIST, blank=True)
    usher_ministry = models.CharField(max_length=25, choices=USHER_MINISTRY_LIST, blank=True)
    usher_ministry_role = models.CharField(max_length=40, choices=USHER_MINISTRY_ROLE_LIST, blank=True)
    worship_ministry =  models.CharField(max_length=25, choices=WORSHIP_MINISTRY_LIST, blank=True)
    worship_ministry_role =  models.CharField(max_length=25, choices=WORSHIP_MINISTRY_ROLE_LIST, blank=True)
    worship_ministry_team =  models.CharField(max_length=25, choices=WORSHIP_MINISTRY_TEAM_LIST, blank=True)
    creative_media = models.CharField(max_length=25, choices=CREATIVE_MEDIA_LIST, blank=True)
    creative_media_role = models.CharField(max_length=25, choices=CREATIVE_MEDIA_ROLE_LIST, blank=True)
    creative_media_team = models.CharField(max_length=25, choices=CREATIVE_MEDIA_TEAM_LIST, blank=True)
    outreach_ministry = models.CharField(max_length=25, choices=OUTREACH_MINISTRY_LIST, blank=True)
    outreach_ministry_role = models.CharField(max_length=25, choices=OUTREACH_MINISTRY_ROLE_LIST, blank=True)
    outreach_ministry_team = models.CharField(max_length=25, choices=OUTREACH_MINISTRY_TEAM_LIST, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class ProfileManager(models.Model):
    pm_functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST)
    pm_manager_name = models.CharField(max_length=50,)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pm_manager_name)

@python_2_unicode_compatible
class FriendsList(models.Model):
    friend = models.ForeignKey(User, default=1)
    friendoffriend = models.CharField(max_length=150, null=True, blank=True,)
    frnd_options = models.CharField(max_length=25, choices=FRIENDS_LIST_OPTIONS)
    requested_date = models.DateTimeField(auto_now=True, null=True, blank=True,)
    frndoffrnd_options = models.CharField(max_length=25, choices=FRIENDS_LIST_OPTIONS)
    accepted_date = models.DateTimeField(auto_now=True, null=True, blank=True,)

    def __str__(self):
        return str(self.friend)


