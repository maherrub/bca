from django.contrib import admin
from userapp.models import *

# Register your models here.


class ProfileManagerAdmin(admin.ModelAdmin):
    fields = ["pm_functional_group", "pm_manager_name",]
    list_display = ["pm_functional_group", "pm_manager_name",]
    list_filter = ["pm_functional_group", "pm_manager_name",]
    search_fields = ["pm_functional_group", "pm_manager_name",]

    class Meta:
        model = ProfileManager


class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = ["sunday_service", "firstname", "lastname", "usermobile", "manager_name", "manager_type","dob",]
    list_filter = ["sunday_service", "firstname", "lastname", "usermobile", "manager_name", "manager_type","dob",]
    search_fields = ["sunday_service", "firstname", "lastname", "usermobile", "manager_name", "manager_type","dob",]

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin) 
admin.site.register(ProfileManager, ProfileManagerAdmin)