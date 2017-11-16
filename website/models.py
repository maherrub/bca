from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import URLValidator

#translation libs
from django.utils.translation import ugettext_lazy 

#website application imports.
from website.choices import *
from .validators import *
#definitions
app_name = 'website'


# models here.
@python_2_unicode_compatible
class HomeGroupManager(models.Model):
    hgp_functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST)
    hgp_manager_name = models.CharField(max_length=50,)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.hgp_manager_name)

@python_2_unicode_compatible
class HomeGroupParallaxImage(models.Model):
    functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST)
    layout = models.CharField(max_length=25, choices=PARALLAX_LAYOUT, default= 'LAON',)
    display_position = models.CharField(max_length=25, choices=PARALLAX_DISPLAY_POSITION_LIST,)
    page_id = models.CharField(max_length=6, null=True, blank=True)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    landscape_background = models.FileField(upload_to='uploads/parallax_images/landscape', validators=[validate_imagefile_extension], null=True, blank=True)
    portrait_background = models.FileField(upload_to='uploads/parallax_images/portrait', validators=[validate_imagefile_extension], null=True, blank=True)
    focus = models.CharField(max_length=25, choices=FOCUS_LIST, default='top center',)
    map1_box_size = models.CharField(max_length=50, null=True, blank=True,)
    map1_coordinate = models.CharField(max_length=50, null=True, blank=True,)
    map1_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    map1_tooltip = models.CharField(max_length=200, null=True, blank=True,)
    map2_box_size = models.CharField(max_length=50, null=True, blank=True,)
    map2_coordinate = models.CharField(max_length=50, null=True, blank=True,)
    map2_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    map2_tooltip = models.CharField(max_length=200, null=True, blank=True,)
    main_text = models.CharField(max_length=100, null=True, blank=True,)
    secondary_text = models.CharField(max_length=200, null=True, blank=True,)
    button_name = models.CharField(max_length=15, null=True, blank=True)
    button_link = models.CharField(max_length=50, null=True, blank=True)
    html_bgcolorcode = models.CharField(max_length=50, null=True, blank=True)
    font_color = models.CharField(max_length=25, blank=True, choices=PAGES_TEXT_COLOR, default='black-text',)
    font_style = models.CharField(max_length=25, blank=True, choices=FONT_LIST, default='font-brush',)
    translatedtxtfile1 = models.FileField(upload_to='uploads/parallax_images/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/parallax_images/', validators=[validate_transfile_extension], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    hgpi_owner = models.ForeignKey(User, editable=True,)
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-edited_on"]

    def __str__(self):
        return str(self.main_text)
    
    def get_absolute_url(self):
        return reverse('phgpi_detail', kwargs={'pk': self.pk})

    

@python_2_unicode_compatible
class HomeGroupTopic(models.Model):
    functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST,)
    layout = models.CharField(max_length=1, choices=CARD_LAYOUT, default='4',)
    display_position = models.CharField(max_length=25, choices=DISPLAY_POSITION_LIST,)
    page_id = models.CharField(max_length=6, null=True, blank=True)
    speaker_image = models.FileField(upload_to='uploads/speaker_images/', validators=[validate_imagefile_extension], null=True, blank=True)
    card_type = models.CharField(max_length=25, choices=CARD_TYPE_LIST, default='Topic',)
    link_url = models.TextField(validators=[URLValidator()], null=True, blank=True)
    cover_image = models.FileField(upload_to='uploads/homegroup_images/', validators=[validate_imagefile_extension], null=True, blank=True)
    youtubeid = models.TextField(max_length=100, null=True, blank=True)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    main_title = models.CharField(max_length=25, null=True, blank=True,)
    secondary_title = models.CharField(max_length=75, null=True, blank=True,)
    speaker_name = models.CharField(max_length=50, null=True, blank=True,)
    day = models.CharField(max_length=15, null=True, blank=True,)
    date = models.CharField(max_length=15, null=True, blank=True,)
    time = models.CharField(max_length=15, null=True, blank=True,)
    venue = models.CharField(max_length=65, null=True, blank=True,)
    short_description = models.TextField(blank=True,)
    long_description = models.TextField(blank=True,)
    card_style = models.CharField(max_length=25, blank=True, choices=CARD_STYLES,)
    card_color = models.CharField(max_length=25, blank=True, choices=BACKGROUND_COLORS,)
    text_color = models.CharField(max_length=25, blank=True, choices=PAGES_TEXT_COLOR,)
    translatedtxtfile1 = models.FileField(upload_to='uploads/topics/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/topics/', validators=[validate_transfile_extension], null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    content_owner = models.ForeignKey(User, editable=True,)
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-edited_on"]

    def __str__(self):
        return str(self.main_title)

    def get_absolute_url(self):
        return reverse('hgtcpdetail', kwargs={'pk': self.pk}) 

@python_2_unicode_compatible
class HomeGroupText(models.Model):
    functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST,)
    display_position_text = models.CharField(max_length=25, choices=DISPLAY_POSITION_TEXT_LIST,)
    page_id = models.CharField(max_length=6, null=True, blank=True)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    main_title_text = models.CharField(max_length=100, null=True, blank=True,)
    secondary_title_text = models.CharField(max_length=200, null=True, blank=True,)
    short_description_text = models.TextField(blank=True,)
    button_name = models.CharField(max_length=15, null=True, blank=True)
    link_url = models.TextField(validators=[URLValidator()], null=True, blank=True)
    translatedtxtfile1 = models.FileField(upload_to='uploads/texts/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/texts/', validators=[validate_transfile_extension], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    content_owner = models.ForeignKey(User, editable=True,)
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-edited_on"]

    def __str__(self):
        return str(self.main_title_text)

    def get_absolute_url(self):
        return reverse('phgtext_detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible    
class Page(models.Model):
    functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST,)
    layout = models.CharField(max_length=25, choices=PAGES_LAYOUT, default= 'BGPF',)
    menu_position = models.CharField(max_length=50, choices=PAGES_DISPLAY_POSITION,)
    menu_name = models.CharField(max_length=25, null=True, blank=True)
    menu_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    youtubeid = models.TextField(max_length=100, null=True, blank=True)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    main_title = models.CharField(max_length=100, null=True, blank=True,)
    high_title = models.CharField(max_length=100, null=True, blank=True,)
    high_title_color = models.CharField(max_length=20, choices=PAGES_TEXT_COLOR,)  
    html_bgcolorcode = models.CharField(max_length=50, null=True, blank=True)
    covermedia =  models.FileField(upload_to='uploads/pages/', validators=[validate_imagefile_extension], null=True, blank=True)
    focus = models.CharField(max_length=25, choices=FOCUS_LIST, default='top center',)
    content = models.TextField(blank=True,)
    left_btnname = models.CharField(max_length=25, null=True, blank=True)
    left_btnlink = models.TextField(validators=[URLValidator()], null=True, blank=True)
    right_btnname = models.CharField(max_length=25, null=True, blank=True)
    right_btnlink = models.TextField(validators=[URLValidator()], null=True, blank=True)
    translatedtxtfile1 = models.FileField(upload_to='uploads/pages/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/pages/', validators=[validate_transfile_extension], null=True, blank=True)
    layout_text = models.CharField(max_length=25, choices=TEXT_LAYOUT, default= 'TLST',)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    owner = models.ForeignKey(User, editable=True,) 
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-edited_on"]

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('producerpage_detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class Extend(models.Model):
    extend_pageid = models.ForeignKey(Page,)
    layout = models.CharField(max_length=25, choices=PAGES_DISPLAY_LAYOUT, default='parallax-style',)
    display_section = models.CharField(max_length=10, choices=PAGES_DISPLAY_SECTION, default='section1',)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    map1_box_size = models.CharField(max_length=50, null=True, blank=True,)
    map1_coordinate = models.CharField(max_length=50, null=True, blank=True,)
    map1_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    map1_tooltip = models.CharField(max_length=200, null=True, blank=True,)
    map2_box_size = models.CharField(max_length=50, null=True, blank=True,)
    map2_coordinate = models.CharField(max_length=50, null=True, blank=True,)
    map2_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    map2_tooltip = models.CharField(max_length=200, null=True, blank=True,)
    main_title = models.CharField(max_length=100, null=True, blank=True,)
    high_title = models.CharField(max_length=100, null=True, blank=True,)
    high_title_color = models.CharField(max_length=20, choices=PAGES_TEXT_COLOR,)  
    extendmedia =  models.FileField(upload_to='uploads/pages/extend', validators=[validate_imagefile_extension], null=True, blank=True)
    focus = models.CharField(max_length=25, choices=FOCUS_LIST, default='top center',)
    content = models.TextField(blank=True,)
    translatedtxtfile1 = models.FileField(upload_to='uploads/extends/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/extends/', validators=[validate_transfile_extension], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    owner = models.ForeignKey(User, editable=True,) 
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["display_section"]

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('producerpageextend_detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class TeamName(models.Model):
    team_pageid = models.ForeignKey(Page,)
    team_name = models.CharField(max_length=100,)
    team_description = models.TextField(blank=True,)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    translatedtxtfile1 = models.FileField(upload_to='uploads/teamnames/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/teamnames/', validators=[validate_transfile_extension], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    owner = models.ForeignKey(User, editable=True,) 
    edited_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.team_name)

    def get_absolute_url(self):
        return reverse('producerpageteam_detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class TeamMember(models.Model):
    teamname_id = models.ForeignKey(TeamName)
    layout = models.CharField(max_length=25, choices=TEAMMEMBER_LAYOUT_TYPE, default='Standard')
    hierarchy = models.CharField(max_length=2, choices=TEAM_MEMBER_HIERARCHY, default='1',)
    member_name = models.CharField(max_length=50, null=True, blank=True)
    member_picture = models.FileField(upload_to='uploads/pages/team/', validators=[validate_imagefile_extension], null=True, blank=True)
    member_title = models.CharField(max_length=50, null=True, blank=True)
    member_crux = models.TextField(blank=True,)
    member_displayposition = models.CharField(max_length=4, choices=MEMBER_DISPLAY_POSITION, default='col1',)
    more_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    form_locale = models.FileField(upload_to='uploads/teammembers/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile1 = models.FileField(upload_to='uploads/teammembers/', validators=[validate_transfile_extension], null=True, blank=True)
    translatedtxtfile2 = models.FileField(upload_to='uploads/teammembers/', validators=[validate_transfile_extension], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    owner = models.ForeignKey(User, editable=True,) 
    edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["member_name"]

    def __str__(self):
        return str(self.member_name)

    def get_absolute_url(self):
        return reverse('producerpageteammember_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class aResource(models.Model):
    functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST,)
    cover = models.FileField(upload_to='uploads/resources/cover/', validators=[validate_imagefile_extension], null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True,)
    title_locale = models.FileField(upload_to='uploads/resources/title/', validators=[validate_transfile_extension], null=True, blank=True)
    author = models.CharField(max_length=25, null=True, blank=True,)
    author_locale = models.FileField(upload_to='uploads/resources/author/', validators=[validate_transfile_extension], null=True, blank=True)
    language = models.CharField(max_length=25, choices=LANGUAGE_LIST, default='English', )
    search_keywords_file = models.FileField(upload_to='uploads/resources/tags/', validators=[validate_transfile_extension], null=True, blank=True)
    genre = models.CharField(max_length=25, choices=GENRE_LIST, default='Sermon', )
    description = models.FileField(upload_to='uploads/resources/description/', validators=[validate_transfile_extension], null=True, blank=True) 
    is_favorite = models.BooleanField(default=False)
    counter = models.IntegerField(default=0,)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    is_featured = models.BooleanField(default=False,)
    owner = models.ForeignKey(User, editable=True,)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.pk})

    
@python_2_unicode_compatible
class aResourceItem(models.Model):
    resource_id = models.ForeignKey(aResource)
    item_name = models.CharField(max_length=50, null=True, blank=True,)
    item_name_locale = models.FileField(upload_to='uploads/resources/item_name/', validators=[validate_transfile_extension], null=True, blank=True)
    file_type = models.CharField(max_length=25, choices=FILE_TYPE_LIST,)
    resource_item = models.FileField(upload_to='downloads/resources/item/', validators=[validate_resourceitem_extension], null=True, blank=True)
    is_published = models.BooleanField(default=False,)
    is_verified = models.BooleanField(default=False,)
    owner = models.ForeignKey(User, editable=True,)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.item_name)

    def get_absolute_url(self):
        return reverse('resourceitem_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Vendor(models.Model):
    project_name = models.CharField(max_length=25, null=True, blank=True,) 
    version = models.CharField(max_length=10, null=True, blank=True,)
    description = models.TextField(null=True, blank=True,)
    developed_by = models.CharField(max_length=25, null=True, blank=True,)
    released_by =  models.CharField(max_length=25, null=True, blank=True,)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, editable=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.project_name + self.version)



    