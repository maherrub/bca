from django import forms
from django.contrib.auth.models import User
from django.forms.extras import SelectDateWidget
from website.models import *
from website.choices import *
from website.views import *


#translation libs
from django.utils.translation import ugettext_lazy 


#django-messages imports
from django_messages.models import Message
from django_messages.fields import CommaSeparatedUserField

app_name = 'website'

#form here.


class HomeGroupTopicForm(forms.ModelForm):
    functional_group = forms.ChoiceField(choices=HG_FUNCTION_GROUP_LIST, initial='English',)
          

    class Meta:
        model = HomeGroupTopic
    
        fields = [
            'functional_group',
            'layout',
            'display_position',
            'page_id',
            'speaker_image',
            'card_type',
            'link_url',
            'cover_image',
            'youtubeid',
            'main_title',
            'secondary_title',
            'speaker_name',
            'day',
            'date',
            'time',
            'venue',
            'short_description',
            'long_description',
            'card_style',
            'card_color',
            'text_color',
            'translatedtxtfile1',
            'translatedtxtfile2',                     
        ]


class PHgTextForm(forms.ModelForm):
    functional_group = forms.ChoiceField(choices=HG_FUNCTION_GROUP_LIST, initial='English',)
    
    class Meta:
        model = HomeGroupText

        fields = [
            'functional_group',
            'display_position_text',
            'page_id',
            'main_title_text',
            'secondary_title_text',
            'short_description_text',
            'button_name',
            'link_url',
            'translatedtxtfile1',
            'translatedtxtfile2',
        ]


class PHgPiForm(forms.ModelForm):
    functional_group = forms.ChoiceField(choices=HG_FUNCTION_GROUP_LIST, initial='English',)
    
    
    class Meta:
        model = HomeGroupParallaxImage
    
        fields = [
            'functional_group',
            'layout',
            'display_position',
            'page_id',
            'landscape_background',
            'portrait_background',
            'focus',
            'map1_box_size',
            'map1_coordinate',
            'map1_link',
            'map1_tooltip',
            'map2_box_size',
            'map2_coordinate',
            'map2_link',
            'map2_tooltip',
            'main_text',
            'secondary_text',
            'button_name',
            'button_link',
            'font_color',
            'font_style',
            'html_bgcolorcode',
            'translatedtxtfile1',
            'translatedtxtfile2',
        ]


class PPageForm(forms.ModelForm):
    high_title_color = forms.ChoiceField(choices=PAGES_TEXT_COLOR, initial='black-text',)
    

    class Meta:
        model = Page

        fields = [
            'functional_group',
            'layout',
            'html_bgcolorcode',
            'menu_position',
            'menu_name',
            'menu_link',
            'youtubeid',
            'main_title',
            'high_title',
            'high_title_color',
            'covermedia',
            'focus',
            'content',
            'left_btnname',
            'left_btnlink',
            'right_btnname',
            'right_btnlink',
            'translatedtxtfile1',
            'translatedtxtfile2',
            'layout_text',
        ]

class TeamNameForm(forms.ModelForm):

    class Meta:
        model = TeamName

        fields = [
            'team_pageid',
            'team_name',
            'team_description',
            'translatedtxtfile2',
        ]

class TeamMemberForm(forms.ModelForm):

    class Meta:
        model = TeamMember

        fields = [
            'teamname_id',
            'layout',
            'hierarchy',
            'member_name',
            'member_picture',
            'member_title',
            'member_crux',
            'member_displayposition',
            'more_link',
            'form_locale',
            'translatedtxtfile2',
            
        ]

class PPExtendForm(forms.ModelForm):

    class Meta:
        model = Extend

        fields = [
            'extend_pageid',
            'layout',
            'display_section',
            'extendmedia',
            'focus',
            'map1_box_size',
            'map1_coordinate',
            'map1_link',
            'map1_tooltip',
            'map2_box_size',
            'map2_coordinate',
            'map2_link',
            'map2_tooltip',
            'main_title',
            'high_title',
            'high_title_color',
            'content',
            'translatedtxtfile1',
            'translatedtxtfile2',

        ]


class ComposeForm(forms.ModelForm):
    recipient = CommaSeparatedUserField(label=(u"Recipient"))
    body = forms.CharField(label=(u"Body"),
        widget=forms.Textarea(attrs={'rows': '12', 'cols':'55'}))

    class Meta:
        model = Message

        fields = [
            'recipient',
            'body',
        ]
    
class aResourceForm(forms.ModelForm):
    
    class Meta:
        model = aResource

        fields = [ 
            'functional_group',
            'cover',
            'title',
            'title_locale',
            'author',
            'author_locale',
            'language',
            'search_keywords_file',
            'genre',
            'description',
            
        ]

class aResourceItemForm(forms.ModelForm):

    class Meta:
        model = aResourceItem

        fields = [
            'resource_id',
            'item_name',
            'item_name_locale',
            'file_type',
            'resource_item',
        ]

