from django import forms
from django.contrib.auth.models import User
from django.forms.extras import SelectDateWidget
from django.forms.extras.widgets import SelectDateWidget
from multiselectfield import MultiSelectField
from helpdesk.models import *
from helpdesk.views import *
from helpdesk.choices import *

app_name = 'helpdesk'

class UserTicketForm(forms.ModelForm):
    
    assigned_manager = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = Ticket

        fields = [  
            'ticket_category', 
            'ticket_priority',
            'ticket_issue', 
            'ticket_description',
            'ticket_screenshot',
            'assigned_manager',
            
            ]


class UserTicketUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Ticket

        fields = [  
            'ticket_priority',
            'ticket_status', 
            'ticket_issue', 
            'ticket_description',
            'ticket_screenshot',
            ]


class TicketManagerForm(forms.ModelForm):

    class Meta:
        model = TicketManager

        fields = [
            'ticket_manager_ticket',
            'ticket_manager_fg',
            'ticket_manager_reply',
            ]

class SupportTicketManagerForm(forms.ModelForm):

    class Meta:
        model = TicketManager

        fields = [
            'ticket_manager_ticket',
            'ticket_manager_fg',
            'ticket_manager_reply',
            
            ]

class ServiceTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'assigned_manager',
        ]

class ManagerTicketForm(forms.ModelForm):

    
    class Meta:
        model = Ticket

        fields = [
            'consent_manager_name',
            'consent_manager_signed',
            'consent_manager_reason',
        ]

class SupportTicketForm(forms.ModelForm):
    

    class Meta:
        model = Ticket

        fields = [
            'ticket_category',
            'consent_manager_name',
            'ticket_priority',
            'ticket_status',
            'assigned_manager',
            
        ]