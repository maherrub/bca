from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.auth.models import User
from functools import partial

#imports from local apps
from website.choices import *
from userapp.models import *
from userapp.choices import *

#django-messages imports
from django_messages.models import *
from django_messages.forms import *


app_name = 'userapp'

DateInput = partial(forms.DateInput, {'class': 'form-control datepicker'})



class UserProfileForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices = SALUTATION_LIST,required=True)
    firstname = forms.CharField(label = 'First Name',)
    lastname = forms.CharField(label = 'Last Name',)
    usercover = forms.FileField(label = 'Profile picture (jpg / png only)',)
    usermobile = forms.CharField(label = 'Mobile Number',)
    address_line1 = forms.CharField(label = 'Apartment Number',)
    address_line2 = forms.CharField(label = 'Street',)
    city_or_town = forms.CharField(label = 'City / Town',)
    state_or_province = forms.CharField(label = 'State / Province',)
    country = forms.CharField(label = 'Country',)
    zip_or_postal_code = forms.CharField(label = 'Zip / Pin',)
    dob = forms.DateField(widget=DateInput(), label = "Date of birth",)
    who_brought_you_here = forms.CharField(label = 'Who brought you here?',)
    whos_mobile_number = forms.CharField(label = 'What is his / her contact number?',)
    sunday_service = forms.ChoiceField(choices=HG_FUNCTION_GROUP_LIST, initial='English', label = "Which sunday service do you attend?",)
    expertise = forms.ChoiceField(choices = EXPERTISE_LIST,required=True, label = "You are expert in",)
    age_group = forms.ChoiceField(choices = AGE_GROUP_LIST,required=True,  label = "Your age group",)
    marital_status = forms.ChoiceField(choices = MARITAL_STATUS_LIST, required=True,  label = "Your Marital Status",)
    number_of_children = forms.ChoiceField(choices = CHILDREN_LIST, required=True,  label = "Number of children",)
    oikos = forms.ChoiceField(choices = OIKOS_LIST, label = "Selct an OIKOS(Cell Group) that is closer to your location",)
    community_services = forms.ChoiceField(choices = COMMUNITY_SERVICES_LIST, label = "Interested in community services?")
    usher_ministry = forms.ChoiceField(choices = USHER_MINISTRY_LIST, label = "Become an usher?")
    worship_ministry = forms.ChoiceField(choices = WORSHIP_MINISTRY_LIST, label = "Join the worship team")
    creative_media = forms.ChoiceField(choices = CREATIVE_MEDIA_LIST, label = "Are you a creative person?")
    outreach_ministry = forms.ChoiceField(choices = OUTREACH_MINISTRY_LIST, label = "Are you a people person?")

    class Meta:
        
        model = UserProfile
       
        fields = [
            'salutation',
            'firstname', 
            'lastname', 
            'usercover', 
            'usermobile',
            'address_line1',
            'address_line2',
            'city_or_town',
            'state_or_province',
            'country',
            'zip_or_postal_code',
            'dob',
            'who_brought_you_here',
            'whos_mobile_number',
            'sunday_service',
            'expertise',
            'age_group',
            'marital_status',
            'number_of_children',
            'oikos',
            'community_services',
            'usher_ministry',
            'worship_ministry',
            'creative_media',
            'outreach_ministry',
            ]


#Profile Managers User Profile Form
class PMUPForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput(), label = "Date of birth",)
    is_leader = forms.ChoiceField(choices = BOOLEAN_LIST,)
    class Meta:
        model = UserProfile

        fields = [
            'user',
            'salutation',
            'firstname', 
            'lastname', 
            'usercover', 
            'usermobile',
            'address_line1',
            'address_line2',
            'city_or_town',
            'state_or_province',
            'country',
            'postal_code',
            'dob',
            'who_brought_you_here',
            'whos_mobile_number',
            'sunday_service',
            'expertise',
            'age_group',
            'marital_status',
            'number_of_children',
            'oikos',
            'oikos_role',
            'community_services',
            'community_services_role',
            'usher_ministry',
            'usher_ministry_role',
            'worship_ministry',
            'worship_ministry_role',
            'worship_ministry_team',
            'creative_media',
            'creative_media_role',
            'creative_media_team',
            'outreach_ministry',
            'outreach_ministry_role',
            'outreach_ministry_team',
            'membership',
            'is_leader',
            'manager_name',
            'manager_type',
            'ticket_manager_name'

        ]





