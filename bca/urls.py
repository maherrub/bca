from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from filebrowser.sites import site

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/filebrowser/', include(site.urls)),
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls')),
    url(r'^up/', include('userapp.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^helpdesk/', include('helpdesk.urls')),
    url(r'^messages/', include('django_messages.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)