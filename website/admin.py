from django.contrib import admin
from website.models import *


# Registering models.

class HomeGroupManagerAdmin(admin.ModelAdmin):
    fields = ["hgp_functional_group", "hgp_manager_name",]
    list_display = ["hgp_functional_group", "hgp_manager_name", "added", "updated",]
    list_filter = ["hgp_functional_group", "hgp_manager_name", "added", "updated",]
    search_fields = ["hgp_functional_group", "hgp_manager_name",]

    class Meta:
        model = HomeGroupManager


class HomeGroupParallaxImageAdmin(admin.ModelAdmin):
    fields = ["functional_group", "layout", "display_position", "page_id", "landscape_background", "focus", "map1_box_size", "map1_coordinate", "map1_link", "map1_tooltip", "map2_box_size", "map2_coordinate", "map2_link", "map2_tooltip", "portrait_background", "main_text", "secondary_text", "button_name", "button_link", "font_color", "font_style", "html_bgcolorcode", "translatedtxtfile1", "translatedtxtfile2", "hgpi_owner", "edited_on",]
    list_display = ["pk", "page_id", "functional_group", "layout", "display_position", "focus", "is_verified", "is_published", "hgpi_owner", "edited_on", "updated",]
    list_editable = ["page_id", "layout", "is_verified", "is_published",]
    list_filter = ["functional_group", "layout", "display_position", "is_verified", "is_published", "edited_on", "updated",]
    search_fields = ["main_text", "secondary_text",]

    class Meta:
        model = HomeGroupParallaxImage

class HomeGroupTopicAdmin(admin.ModelAdmin):
    fiedls = ["functional_group", "layout", "display_position", "card_type", "page_id",  "link_url", "speaker_image", "cover_image", "youtubeid", "main_title", "secondary_title", "speaker_name", "day", "date", "time", "venue", "short_description", "long_description", "card_style", "card_color", "text_color", "translatedtxtfile1", "translatedtxtfile2",]
    list_display = ["pk", "page_id", "layout", "functional_group", "display_position", "card_type", "main_title", "is_verified", "is_published", "content_owner", "updated",]
    list_editable = ["page_id", "is_verified", "is_published", "content_owner",]
    list_filter = ["functional_group", "display_position", "layout", "card_type", "main_title", "content_owner", "edited_on", "updated",]
    search_fields = ["functional_group", "display_position",  "main_title", "content_owner", "secondary_title", "short_description", "long_description",]

    class Meta:
        model = HomeGroupTopic

class HomeGroupTextAdmin(admin.ModelAdmin):
    fields = ["functional_group", "display_position_text", "page_id", "main_title_text", "secondary_title_text", "short_description_text", "button_name", "link_url", "translatedtxtfile1", "translatedtxtfile2", "content_owner",]
    list_display = ["pk", "page_id", "functional_group", "display_position_text", "is_verified", "is_published", "content_owner", "edited_on", "updated",]
    list_editable = ["page_id", "is_verified", "is_published", "content_owner",]
    list_filter = ["functional_group", "display_position_text", "main_title_text", "content_owner", "edited_on", "updated",]
    search_fields = ["functional_group", "display_position_text", "main_title_text", "secondary_title_text", "short_description_text",]

    class Meta:
        model = HomeGroupText

class PageAdmin(admin.ModelAdmin):
    fields = ["functional_group", "layout", "html_bgcolorcode", "menu_position", "menu_name", "menu_link", "youtubeid", "main_title", "high_title", "high_title_color", "covermedia", "focus", "content", "left_btnname", "left_btnlink", "right_btnname", "right_btnlink", "translatedtxtfile1", "translatedtxtfile2", "layout_text", "owner", "edited_on",]
    list_display = ["id", "functional_group", "menu_position", "menu_name", "menu_link", "youtubeid", "focus", "is_verified", "is_published", "owner", "edited_on", "updated",]
    list_editable = ["is_verified", "is_published",]
    list_filter = ["functional_group", "menu_position", "main_title", "layout", "focus", "layout_text", "owner", "edited_on", "updated",]
    search_fields = ["main_title", "high_title", "content", "menu_name", "owner",]

    class Meta:
        model = Page

class TeamNameAdmin(admin.ModelAdmin):
    fields = ["team_pageid", "team_name", "team_description", "is_published", "is_verified", "translatedtxtfile1", "translatedtxtfile2", "owner", "edited_on",]
    list_display = ["team_pageid", "team_name", "is_published", "is_verified", "owner", "edited_on", "updated",]
    list_editable = ["team_name", "is_published", "is_verified",]
    list_filter = ["team_name", "edited_on", "updated",]

    class Meta:
        model = TeamName

class TeamMemberAdmin(admin.ModelAdmin):
    fields = ["teamname_id", "layout", "hierarchy", "member_name", "member_picture", "member_title", "member_crux", "member_displayposition", "more_link", "form_locale", "translatedtxtfile1", "translatedtxtfile2", "owner", "edited_on",]
    list_display = ["teamname_id", "layout", "hierarchy", "member_name", "member_displayposition", "owner", "edited_on", "updated",]
    list_editable = ["hierarchy", "member_displayposition",]
    list_filter = ["teamname_id", "hierarchy", "member_name", "member_title", "edited_on", "updated",]
    search_fields = ["teamname_id", "member_name", "member_crux",]

    class Meta:
        model = TeamMember


class ExtendAdmin(admin.ModelAdmin):
    fields = ["extend_pageid", "layout", "display_section", "is_published", "is_verified", "extendmedia", "focus", "map1_box_size", "map1_coordinate", "map1_link", "map1_tooltip", "map2_box_size", "map2_coordinate", "map2_link", "map2_tooltip", "main_title", "high_title", "high_title_color", "content", "translatedtxtfile1", "translatedtxtfile2", "owner", "edited_on",]
    list_display = ["pk", "extend_pageid", "layout", "display_section", "focus", "is_published", "is_verified", "main_title", "owner", "edited_on", "updated",]
    list_editable = ["extend_pageid", "layout", "display_section",]
    list_filter = ["extend_pageid", "display_section", "is_published", "is_verified", "owner", "edited_on", "updated",]
    search_fields = ["main_title", "high_title", "content", "owner",]
    
    class Meta:
        model = Extend


class aResourceAdmin(admin.ModelAdmin):
    fields = ["functional_group", "is_published", "is_verified", "is_featured", "cover", "title", "title_locale", "author", "author_locale", "language", "search_keywords_file", "genre", "description", "is_favorite", "counter", "owner", "created",]
    list_display = ["pk", "functional_group", "title", "is_published", "is_verified", "is_featured", "author", "genre", "owner", "updated", "created",] 
    list_editable = ["is_published", "is_verified", "is_featured",]
    list_filter = ["functional_group", "author", "language", "genre", "owner", "updated", "created", ]
    search_fields = ["title",]
    
    class Meta:
        model = aResource

class aResourceItemAdmin(admin.ModelAdmin):
    fields = ["resource_id", "item_name", "item_name_locale", "file_type", "resource_item", "is_published", "is_verified", "owner", "created",]
    list_display = ["pk", "resource_id", "file_type", "item_name", "is_published", "is_verified", "owner", "updated", "created",]
    list_editable = ["is_published", "is_verified",]
    list_filter = ["resource_id", "file_type", "is_published", "is_verified", "owner", "updated", ]
    search_fields = ["item_name",]

    class Meta:
        model = aResourceItem

class VendorAdmin(admin.ModelAdmin):
    fields = ["project_name", "version", "description", "developed_by", "released_by", "created"]
    list_display = ["project_name", "version", "released_by", "updated", "created",]
    list_editable = ["project_name", "version", "released_by",]
    list_filter = ["project_name", "version","developed_by", "updated", "created",]

    class Meta:
        model = Vendor

admin.site.register(HomeGroupManager, HomeGroupManagerAdmin)
admin.site.register(HomeGroupParallaxImage, HomeGroupParallaxImageAdmin)
admin.site.register(HomeGroupTopic, HomeGroupTopicAdmin)
admin.site.register(HomeGroupText, HomeGroupTextAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Extend, ExtendAdmin)
admin.site.register(TeamName, TeamNameAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(aResource, aResourceAdmin)
admin.site.register(aResourceItem, aResourceItemAdmin)
admin.site.register(Vendor, VendorAdmin)
