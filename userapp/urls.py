from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from userapp.views import *

app_name = 'userapp'

urlpatterns = [
    
    
    url(r'^up_list$', UpList.as_view(), name='up_list'),
    url(r'^up_create$', UpCreate.as_view(), name='up_create'),
    url(r'^up_detail/(?P<pk>[-\w]+)/$', UpDetail.as_view(), name='up_detail'),
    url(r'^(?P<pk>[-\w]+)/$', UpDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$', UpUpdate.as_view(), name='update'),
    
    url(r'^pm_console$', PMCView, name='pm_console'),
    url(r'^pmlv/(?P<fg>[\w-]+)/$', PMUpList.as_view(), name='pmlv',),
    url(r'^socialmediauserlist/(?P<fg>[\w-]+)/$', SocialMediaUserList.as_view(), name='socialmediauserlist',),
    url(r'^up_list/(?P<fg>[\w-]+)/$', SocialMediaUserList.as_view(), name='up_list',),
    url(r'^(?P<pk>\d+)/pmup_detail$', PMUPUpdate.as_view(), name='pmup_detail'),
    
]