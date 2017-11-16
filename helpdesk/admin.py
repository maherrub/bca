from django.contrib import admin
from django.contrib.admin.widgets import AdminTextInputWidget, AdminTextareaWidget
from helpdesk.models import *
from helpdesk.choices import *

# Register your models here.

class HelpDeskManagerAdmin(admin.ModelAdmin):
    fields = ['hdmgr_functional_group', 'hdmgr_functional_group_area', 'hdmgr_ticket_manager_name',]
    list_display = ['hdmgr_functional_group', 'hdmgr_functional_group_area', 'hdmgr_ticket_manager_name', ]
    
       

class TicketAdmin(admin.ModelAdmin):
    
    fields = ['ticket_category', 'ticket_issue', 'ticket_priority', 'ticket_status', 'ticket_screenshot', 'ticket_description', 'ticket_owner', 'consent_manager_key', 'consent_manager_name', 'consent_manager_signed', 'assigned_manager', 'ticket_edited_on',]
    list_display = ['ticket_category', 'ticket_number', 'ticket_owner', 'ticket_issue', 'ticket_priority', 'ticket_status', 'consent_manager_name', 'consent_manager_signed', 'assigned_manager',]
    list_editable = ['ticket_priority', 'ticket_status', 'assigned_manager', 'consent_manager_signed',]
    list_filter = ['ticket_category', 'ticket_number', 'ticket_priority', 'ticket_status', 'ticket_owner', 'ticket_edited_on',]
    search_fields = ['ticket_number', 'ticket_description', 'ticket_owner',]



class TicketManagerAdmin(admin.ModelAdmin):
    fields = ['ticket_manager_ticket', 'ticket_manager_fg', 'ticket_manager_reply', 'ticket_manager_name',]
    list_display = ['ticket_manager_fg', 'ticket_manager_reply', 'ticket_manager_ticket', 'ticket_manager_edited_on', 'ticket_manager_name']
    



admin.site.register(HelpDeskManager, HelpDeskManagerAdmin)
admin.site.register(TicketManager, TicketManagerAdmin)
admin.site.register(Ticket, TicketAdmin)
