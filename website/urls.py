from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import activate
from website.views import *

app_name = 'website'


urlpatterns = [
    
    url(r'^$', english_home, name='en'),
    url(r'^cn/$', chinese_home, name='cn'),
    url(r'^hk/$', hokkien_home, name='hk'),
    url(r'^ct/$', cantonese_home, name='ct'),
    url(r'^in/$', indian_home, name='in'),
    url(r'^fp/$', filipino_home, name='fp'),
    url(r'^iot/$', iot_home, name='iot'),
    
    
    
    
    #url(r'^apps_list/$', apps, name='apps_list'),
    url(r'^apps_list/$', AppsView.as_view(), name='apps_list'),
    url(r'^Success/$', success, name='Success'),
    url(r'^None/$', none, name='None'),
   

    url(r'^producer/$', producer, name='producer'),
    url(r'^downloadresource/$', DownloadResourceList.as_view(), name='downloadresource'),
    url(r'^bcareleases/$', BCAReleaseList.as_view(), name='bcareleases'),
    url(r'^producercommunity/$', producercommunity, name='producercommunity'),
    
    url(r'^phgtl/(?P<fg>[\w-]+)/$', PHgTList.as_view(), name='phgt_list',),
    
    url(r'^hgtopic_list/$', HgtopicsList.as_view(), name='hgtopic_list',),

    
    url(r'^phgpi_create/(?P<fg>[\w-]+)/$', PHgPiCreate.as_view(), name='phgpi_create',),
    url(r'^phgtext_create/(?P<fg>[\w-]+)/$', PHgTextCreate.as_view(), name='phgtext_create',),
    url(r'^phgtopic_create/(?P<fg>[\w-]+)/$', HgtopicsCreate.as_view(), name='phgtopic_create',),
    url(r'^producerpage_create/(?P<fg>[\w-]+)/$', PPageCreate.as_view(), name='producerpage_create',),
    url(r'^producerpageteam_create/(?P<fg>[\w-]+)/$', TeamNameCreate.as_view(), name='producerpageteam_create',),
    url(r'^producerpageteammember_create/(?P<fg>[\w-]+)/$', TeamMemberCreate.as_view(), name='producerpageteammember_create',),
    url(r'^producerpageextend_create/(?P<fg>[\w-]+)/$', PPExtendCreate.as_view(), name='producerpageextend_create',),
    url(r'^resource_create/(?P<fg>[\w-]+)/$', ResourceCreate.as_view(), name='resource_create',),
    url(r'^resourceitem_create/(?P<fg>[\w-]+)/$', ResourceItemCreate.as_view(), name='resourceitem_create',),
    
    url(r'^(?P<pk>[-\w]+)/$',HgtopicsDetail.as_view(), name='hgtdetail',),
    url(r'^None/hgtcpdetail$', none, name='None'),
    url(r'^(?P<pk>[-\w]+)/hgtcpdetail$',HgtopicsCpDetail.as_view(), name='hgtcpdetail',),
    url(r'^(?P<pk>[-\w]+)/producerpage_detail$',PPageDetail.as_view(), name='producerpage_detail',),
    url(r'^(?P<pk>[-\w]+)/producerpageteam_detail$',TeamNameDetail.as_view(), name='producerpageteam_detail',),
    url(r'^(?P<pk>[-\w]+)/bcpublicpage$',PublicPageDetail.as_view(), name='bcpublicpage',),
    
    
    url(r'^phgtext_list/(?P<fg>[\w-]+)/$', PHgTextList.as_view(), name='phgtext_list',),
    url(r'^phgpi_list/(?P<fg>[\w-]+)/$', PHgPiList.as_view(), name='phgpi_list',),
    url(r'^producerpage_list/(?P<fg>[\w-]+)/$', PPageList.as_view(), name='producerpage_list',),
    url(r'^(?P<pg>[-\w]+)/producerpageteam_list$', TeamNameList.as_view(), name='producerpageteam_list',),
    url(r'^(?P<pg>[-\w]+)/producerpageextend_list$', PPExtendList.as_view(), name='producerpageextend_list',),
    url(r'^(?P<pg>[-\w]+)/producerpageteammember_list$', TeamMemberList.as_view(), name='producerpageteammember_list',),
    url(r'^pclat/(?P<fg>[\w-]+)/$', PCLATList.as_view(), name='pclat',),
    url(r'^pclatxt/(?P<fg>[\w-]+)/$', PCLATXTList.as_view(), name='pclatxt',),
    url(r'^pclapx/(?P<fg>[\w-]+)/$', PCLAPXList.as_view(), name='pclapx',),
    url(r'^pclapg/(?P<fg>[\w-]+)/$', PCLAPGList.as_view(), name='pclapg',),
    url(r'^pclaex/(?P<fg>[\w-]+)/$', PCLAEXList.as_view(), name='pclaex',),
    url(r'^pclatm/(?P<fg>[\w-]+)/$', PCLATMList.as_view(), name='pclatm',),
    url(r'^pclatmem/(?P<fg>[\w-]+)/$', PCLATMEMList.as_view(), name='pclatmem',),
    url(r'^resource_list/(?P<fg>[\w-]+)/$', ResourceList.as_view(), name='resource_list',),
    url(r'^(?P<pg>[-\w]+)/resourceitem_list$', ResourceItemList.as_view(), name='resourceitem_list',),
    
    url(r'^(?P<pk>[-\w]+)/phgtext_detail$',PHgTextDetail.as_view(), name='phgtext_detail',),
    url(r'^(?P<pk>[-\w]+)/phgpi_detail$',PHgPiDetail.as_view(), name='phgpi_detail',),
    url(r'^(?P<pk>[-\w]+)/producerpageteammember_detail$',TeamMemberDetail.as_view(), name='producerpageteammember_detail',),
    url(r'^(?P<pk>[-\w]+)/producerpageextend_detail$',PPExtendDetail.as_view(), name='producerpageextend_detail',),
    url(r'^(?P<pk>[-\w]+)/resource_detail$',ResourceDetail.as_view(), name='resource_detail',),
    url(r'^(?P<pk>[-\w]+)/resourceitem_detail$',ResourceItemDetail.as_view(), name='resourceitem_detail',),
    url(r'^(?P<pk>[-\w]+)/downloadresource_item$',DownloadResourceItemDetail.as_view(), name='downloadresource_item',),


    url(r'^(?P<pk>[-\w]+)/producerpage_update$',PPageUpdate.as_view(), name='producerpage_update',),
    url(r'^(?P<pk>[-\w]+)/producerhgt_update$',HgtopicsUpdate.as_view(), name='producerhgt_update',),
    url(r'^(?P<pk>[-\w]+)/phgtext_update$',PHgTextUpdate.as_view(), name='phgtext_update',),
    url(r'^(?P<pk>[-\w]+)/phgpi_update$',PHgPiUpdate.as_view(), name='phgpi_update',),
    url(r'^(?P<pk>[-\w]+)/producerpageteam_update$',TeamNameUpdate.as_view(), name='producerpageteam_update',),
    url(r'^(?P<pk>[-\w]+)/producerpageextend_update$',PPExtendUpdate.as_view(), name='producerpageextend_update',),
    url(r'^(?P<pk>[-\w]+)/producerpageteammember_update$',TeamMemberUpdate.as_view(), name='producerpageteammember_update',),
    url(r'^(?P<pk>[-\w]+)/resource_update$',ResourceUpdate.as_view(), name='resource_update',),
    url(r'^(?P<pk>[-\w]+)/resourceitem_update$',ResourceItemUpdate.as_view(), name='resourceitem_update',),

    url(r'^(?P<pk>[-\w]+)/producerpageteammember_delete$',TeamMemberDelete.as_view(), name='producerpageteammember_delete',),


]