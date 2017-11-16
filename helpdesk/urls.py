from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from helpdesk.views import *

app_name = 'helpdesk'

urlpatterns = [
    #url(r'^hd/$', hd, name='hd'),

    #url(r'^ticket_list/$', TicketList.as_view(), name='ticket_list'),
    url(r'^userticket_list/$', UserTicketList.as_view(), name='userticket_list'),
    url(r'^serviceticket_list/$', ServiceTicketList.as_view(), name='serviceticket_list'),
    url(r'^managerticket_list/$', ManagerTicketList.as_view(), name='managerticket_list'),
    url(r'^supportticket_list/$', SupportTicketList.as_view(), name='supportticket_list'),

    #url(r'^ticket_create$', TicketCreate.as_view(), name='ticket_create'),
    #url(r'^(?P<pk>[-\w]+)/ticket_detail$', TicketDetail.as_view(), name='ticket_detail'),

    url(r'^userticket_create$', UserTicketCreate.as_view(), name='userticket_create'),
    
    url(r'^(?P<pk>[-\w]+)/userticket_detail$', UserTicketDetail.as_view(), name='userticket_detail'),
    url(r'^(?P<pk>[-\w]+)/serviceticket_detail$', ServiceTicketDetail.as_view(), name='serviceticket_detail'),
    url(r'^(?P<pk>[-\w]+)/ticketmanager_detail$', TicketManagerDetail.as_view(), name='ticketmanager_detail'),
    url(r'^(?P<pk>[-\w]+)/managerticket_detail$', ManagerTicketDetail.as_view(), name='managerticket_detail'),
    url(r'^(?P<pk>[-\w]+)/supportticket_detail$', SupportTicketDetail.as_view(), name='supportticket_detail'),

    #url(r'^(?P<pk>[-\w]+)/$', TicketDetail.as_view(), name='ticket_details'),
    #url(r'^ticket_update/(?P<pk>[-\w]+)/$', TicketUpdate.as_view(), name='ticket_update'),

    url(r'^(?P<pk>[-\w]+)/userticket_update$', UserTicketUpdate.as_view(), name='userticket_update'),
    url(r'^(?P<pk>[-\w]+)/serviceticket_update$', ServiceTicketUpdate.as_view(), name='serviceticket_update'),
    url(r'^(?P<pk>[-\w]+)/managerticket_update$', ManagerTicketUpdate.as_view(), name='managerticket_update'),
    url(r'^(?P<pk>[-\w]+)/supportticket_update$', SupportTicketUpdate.as_view(), name='supportticket_update'),


    

    url(r'^ticket_manager_create/(?P<fg>[\w-]+)/$', TicketManagerCreate.as_view(), name='ticket_manager_create'),
    url(r'^supportticketmanager_reply/(?P<fg>[\w-]+)/$', SupportTicketManagerCreate.as_view(), name='supportticketmanager_reply'),
]
urlpatterns = format_suffix_patterns(urlpatterns)