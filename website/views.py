from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from multiselectfield import MultiSelectField
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.db.models import Q

#arduino project
import serial #Importing the serial library
#from visual import * #Importing all the vPython library

#date time definitions
from datetime import *


today = date.today()
yesterday = today - timedelta(1)
last7day = today - timedelta(7)
last31day = today - timedelta(31)
last31dayo = last7day - timedelta(31) 
last365day = today - timedelta(365)


#language support
from django.utils.translation import ugettext, ungettext

#userapp imports
from userapp.views import *
from helpdesk.models import *

#website imports
from website.models import *
from website.choices import *
from website.forms import *

#django-messages imports
from django_messages.models import *
from django_messages.forms import *



#definitions
app_name = 'website'

#pagination libraries
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#-------All defs and classes below----#
#-------All Detail Views below--------#


#producer home group parallax image list
class PHgPiList(ListView):
    model = HomeGroupParallaxImage
    template_name = 'website/phgpi_list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super(PHgPiList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'], hgpi_owner=self.request.user).distinct()

#producer home group text list
class PHgTextList(ListView):
    model = HomeGroupText
    template_name = 'website/phgtext_list.html'
    paginated_by = 20

    def get_queryset(self):
        qs = super(PHgTextList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'], content_owner=self.request.user)

#home group text list view?
class HgTextList(ListView):
    model = HomeGroupText
    paginate_by = 20

#public home group topic list?
class HgtopicsList(ListView):
    model = HomeGroupTopic
    paginate_by = 20

#producer home group topic list
class PHgTList(ListView):
    model = HomeGroupTopic
    template_name = 'website/phgtopic_list.html' 
    paginate_by = 20

    def get_queryset(self):
        qs = super(PHgTList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'], content_owner=self.request.user)

#producer pages list view
class PPageList(ListView):
    model = Page
    paginated_by = 20
    template_name = 'website/producerpage_list.html'

    def get_queryset(self):
        qs = super(PPageList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'] , owner=self.request.user)

#producer page team list
class TeamNameList(ListView):
    model = TeamName
    paginated_by = 20
    context_object_name = 'teamname_objects'
    template_name = 'website/producerpageteam_list.html'
    
    def get_queryset(self):
        qs = super(TeamNameList, self).get_queryset()
        return qs.filter(team_pageid=self.kwargs['pg'], owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(TeamNameList, self).get_context_data(**kwargs)
        context['page_objects'] = Page.objects.filter(pk = self.kwargs['pg'])
        return context

#producer page team member list
class TeamMemberList(ListView):
    model = TeamMember
    paginate_by = 20
    template_name = 'website/producerpageteammember_list.html'

    def get_queryset(self):
        qs = super(TeamMemberList, self).get_queryset()
        return qs.filter(teamname_id = self.kwargs['pg'], owner=self.request.user)

#producer page extend list
class PPExtendList(ListView):
    model = Extend
    paginated_by = 20
    context_object_name = 'extend_objects'
    template_name = 'website/producerpageextend_list.html'

    def get_queryset(self):
        qs = super(PPExtendList, self).get_queryset()
        return qs.filter(extend_pageid=self.kwargs['pg'])
   
    def get_context_data(self, **kwargs):
        context = super(PPExtendList, self).get_context_data(**kwargs)
        context['page_objects'] = Page.objects.filter(pk = self.kwargs['pg'])[:1]
        return context


#producer community list all topics with search
class PCLATList(ListView):
    model = HomeGroupTopic
    paginated_by = 20
    template_name = 'website/producercommunitytopiclistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLATList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(main_title__icontains=query)|
                Q(secondary_title__icontains=query)|
                Q(short_description__icontains=query)|
                Q(long_description__icontains=query)|
                Q(link_url__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(display_position__icontains=query)|
                Q(id__icontains=query)|
                Q(functional_group__icontains=query)|
                Q(is_published__icontains=query)

                ).distinct()
        return qs.filter()

#producer community list all texts with search
class PCLATXTList(ListView):
    model = HomeGroupText
    paginated_by = 20
    template_name = 'website/producercommunitytextlistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLATXTList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(main_title_text__icontains=query)|
                Q(secondary_title_text__icontains=query)|
                Q(short_description_text__icontains=query)|
                Q(link_url__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(display_position_text__icontains=query)|
                Q(id__icontains=query)|
                Q(button_name__icontains=query)|
                Q(functional_group__icontains=query)|
                Q(is_published__icontains=query)

                ).distinct()
        return qs.filter()

#producer community list all parallax with search
class PCLAPXList(ListView):
    model = HomeGroupParallaxImage
    paginated_by = 20
    template_name = 'website/producercommunityparallaxlistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLAPXList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(hgpi_name__icontains=query)|
                Q(hgpi_image_main_text__icontains=query)|
                Q(hgpi_image_secondary_text__icontains=query)|
                Q(hgpi_link__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(display_position__icontains=query)|
                Q(id__icontains=query)|
                Q(hgpi_link_button_name__icontains=query)|
                Q(functional_group__icontains=query)|
                Q(is_published__icontains=query)

                ).distinct()
        return qs.filter()

#producer community list all main pages with search
class PCLAPGList(ListView):
    model = Page
    paginated_by = 20
    template_name = 'website/producercommunitypagelistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLAPGList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(main_title__icontains=query)|
                Q(high_title__icontains=query)|
                Q(content__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(menu_position__icontains=query)|
                Q(id__icontains=query)|
                Q(left_btnname__icontains=query)|
                Q(right_btnname__icontains=query)|
                Q(menu_name__icontains=query)|
                Q(functional_group__icontains=query)|
                Q(is_published__icontains=query)

                ).distinct()
        return qs.filter()

#producer community list all extended pages with search
class PCLAEXList(ListView):
    model = Extend
    paginated_by = 20
    template_name = 'website/producercommunityextendlistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLAEXList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(main_title__icontains=query)|
                Q(high_title__icontains=query)|
                Q(content__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(id__icontains=query)|
                Q(layout__icontains=query)|
                Q(display_section__icontains=query)|
                Q(is_published__icontains=query)

                ).distinct()
        return qs.filter()

#producer community list all team names with search
class PCLATMList(ListView):
    model = TeamName
    paginated_by = 20
    template_name = 'website/producercommunityteamlistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLATMList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(team_name__icontains=query)|
                Q(team_description__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(id__icontains=query)
                ).distinct()
        return qs.filter()


#producer community list all team members with search
class PCLATMEMList(ListView):
    model = TeamMember
    paginated_by = 20
    template_name = 'website/producercommunityteammemberlistall.html'

    def get_queryset(self, **kwargs):
        qs = super(PCLATMEMList, self).get_queryset(**kwargs)
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(member_name__icontains=query)|
                Q(member_title__icontains=query)|
                Q(member_crux__icontains=query)|
                Q(hierarchy__icontains=query)|
                Q(edited_on__icontains=query)|
                Q(id__icontains=query)
                ).distinct()
        return qs.filter()


#resource list view
class ResourceList(ListView):
    model = aResource
    paginated_by = 20
    template_name = 'website/resource_list.html'

    def get_queryset(self):
        qs = super(ResourceList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'] , owner=self.request.user)


#resource item list view
class ResourceItemList(ListView):
    model = aResourceItem
    paginated_by = 20
    template_name = 'website/resourceitem_list.html'

    def get_queryset(self):
        qs = super(ResourceItemList, self).get_queryset()
        return qs.filter(resource_id = self.kwargs['pg'], owner=self.request.user)

#resources for download

class DownloadResourceList(ListView):
    model = aResource
    paginate_by = 20
    template_name = 'website/downloadresource_list.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(DownloadResourceList, self).get_context_data(**kwargs)
        context['resource_tw'] = aResource.objects.filter(is_published='True', is_verified='True', created__gte = last7day)
        context['resource_featured'] = aResource.objects.filter(is_published='True', is_verified='True', is_featured ='True')
        context['resource_201707'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=[last31day, last7day])
        context['resource_2017Q1'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=["2017-01-01", "2017-03-31"])
        context['resource_2017Q2'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=["2017-04-01", "2017-06-30"])
        context['resource_2017Q3'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=["2017-07-01", "2017-09-30"])
        context['resource_2017Q4'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=["2017-10-01", "2017-12-31"])
        context['resource_2018Q1'] = aResource.objects.filter(is_published='True', is_verified='True', created__range=["2018-01-01", "2018-03-31"])
        return context

#vendor releases
class BCAReleaseList(ListView):
    model = Vendor
    paginated_by = 20
    template_name = 'bcarelease_list.html'


#-------All Detail Views below--------#
#producer home group parallax image detail
class PHgPiDetail(DetailView):
    model = HomeGroupParallaxImage
    template_name = 'website/phgpi_detail.html'

#producer home group text detail
class PHgTextDetail(DetailView):
     model = HomeGroupText
     template_name = 'website/phgtext_detail.html'

# for home group topic public user?
class HgtopicsDetail(DetailView):
    model = HomeGroupTopic

# producer home group topic detail
class HgtopicsCpDetail(DetailView):
    model = HomeGroupTopic
    template_name = 'website/homegrouptopiccp_detail.html'

#producer page detail view
class PPageDetail(DetailView):
    model = Page
    context_object_name = 'page_objects'
    template_name = 'website/producerpage_detail.html'


    def get_context_data(self, **kwargs):
        context = super(PPageDetail, self).get_context_data(**kwargs)
        context['teamname_objects'] = TeamName.objects.filter(team_pageid = self.kwargs['pk'])
        context['teammembers_objects'] = TeamMember.objects.all()
        context['extend_objects'] = Extend.objects.filter(extend_pageid = self.kwargs['pk'])
        context['parallaxes'] = HomeGroupParallaxImage.objects.filter(page_id = self.kwargs['pk'], functional_group='All', )
        context['texts'] = HomeGroupText.objects.filter(page_id = self.kwargs['pk'], functional_group='All',)
        context['hgtopics'] = HomeGroupTopic.objects.filter(page_id = self.kwargs['pk'],functional_group='All',)
        context['enmenus'] = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
        context['menus'] = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
        context['uprofile']  = UserProfile.objects.order_by('firstname', '-created',)    
        return context

#public page detail 
class PublicPageDetail(DetailView):
    model = Page
    context_object_name = 'page_objects'
    queryset = Page.objects.filter(is_published='True', is_verified='True',)
    
    template_name = 'website/bcpublicpage.html'


    def get_context_data(self, **kwargs):
        context = super(PublicPageDetail, self).get_context_data(**kwargs)
        context['teamname_objects'] = TeamName.objects.filter(team_pageid = self.kwargs['pk'], is_published='True', is_verified='True',)
        context['teammembers_objects'] = TeamMember.objects.all()
        context['extend_objects'] = Extend.objects.filter(extend_pageid = self.kwargs['pk'], is_published='True', is_verified='True',)
        context['parallaxes'] = HomeGroupParallaxImage.objects.filter(page_id = self.kwargs['pk'], functional_group='All', is_published='True', is_verified='True',)
        context['texts'] = HomeGroupText.objects.filter(page_id = self.kwargs['pk'], functional_group='All', is_published='True', is_verified='True',)
        context['hgtopics'] = HomeGroupTopic.objects.filter(page_id = self.kwargs['pk'],functional_group='All', is_published='True', is_verified='True',)
        context['enmenus'] = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
        context['menus'] = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
        context['uprofile']  = UserProfile.objects.order_by('firstname', '-created',)    
        #youtube = Page.objects.filter(youtubeid__exact='').count()
        #if youtube > 0:
            #msg = messages.warning(self.request,'On mobile devices menu may be temporarily disabled by the video, please scroll down to activate the menu')
        return context


#producer page team name detail
class TeamNameDetail(DetailView):
    model = TeamName
    template_name = 'website/producerpageteam_detail.html'

#producer page extend detail
class PPExtendDetail(DetailView):
    model = Extend
    template_name = 'website/producerpageextend_detail.html'
    context_object_name = 'eo'

#producer page team member detail
class TeamMemberDetail(DetailView):
    model = TeamMember
    template_name = 'website/producerpageteammember_detail.html'

#producer page team member detail
class ResourceDetail(DetailView):
    model = aResource
    template_name = 'website/resource_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceDetail, self).get_context_data(**kwargs)
        context['item_objects'] = aResourceItem.objects.filter(resource_id = self.kwargs['pk'])
        return context

#producer page team member detail
class ResourceItemDetail(DetailView):
    model = aResourceItem
    template_name = 'website/resourceitem_detail.html'


class DownloadResourceItemDetail(DetailView):
    model = aResource
    template_name = 'website/downloadresourceitem_detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(DownloadResourceItemDetail, self).get_context_data(**kwargs)
        context['item_objects'] = aResourceItem.objects.filter(resource_id = self.kwargs['pk'])
        return context


#-------All Create Views below--------#
#producer home group parallax image create
class PHgPiCreate(CreateView):
    model = HomeGroupParallaxImage
    form_class = PHgPiForm
    template_name = 'website/phgpi_form.html'

    def get_initial(self):
        initials = super(PHgPiCreate, self).get_initial()
        initials['functional_group'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.hgpi_owner = self.request.user
        self.object.save()
        messages.success(self.request,'Parallax background has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        fg = self.kwargs['fg']
        return reverse('phgpi_list', kwargs={'fg': fg})

#producer home group text create
class PHgTextCreate(CreateView):
    model = HomeGroupText
    form_class = PHgTextForm
    template_name = 'website/phgtext_form.html'

    def get_initial(self):
        initials = super(PHgTextCreate, self).get_initial()
        initials['functional_group'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.content_owner = self.request.user
        self.object.save()
        messages.success(self.request,'Text area or Testimonial has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        fg = self.kwargs['fg']
        return reverse('phgtext_list', kwargs={'fg': fg})


# producer home group topic create
class HgtopicsCreate(CreateView):
    model = HomeGroupTopic
    form_class = HomeGroupTopicForm

    def get_initial(self):
        initials = super(HgtopicsCreate, self).get_initial()
        initials['functional_group'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.content_owner = self.request.user
        self.object.save()
        messages.success(self.request,'Topic has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        fg = self.kwargs['fg']
        return reverse('phgtl', kwargs={'fg': fg})

#producer page create 
class PPageCreate(CreateView):
    model = Page
    form_class = PPageForm
    template_name = 'website/producerpage_form.html'

    def get_initial(self):
        initials = super(PPageCreate, self).get_initial()
        initials['functional_group'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Main Page has been successfully created!')
        return redirect(self.object)


#producer page team name create        
class TeamNameCreate(CreateView):
    model = TeamName
    form_class = TeamNameForm
    template_name = 'website/producerpageteam_form.html'

    def get_initial(self):
        initials = super(TeamNameCreate, self).get_initial()
        initials['team_pageid'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Team Name has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('producerpage_detail', kwargs={'pk': pk})


#producer page team member create
class TeamMemberCreate(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'website/producerpageteammember_form.html'

    def get_initial(self):
        initials = super(TeamMemberCreate, self).get_initial()
        initials['teamname_id'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Team Member has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('producerpage_detail', kwargs={'pk': pk})


#producer page extend create
class PPExtendCreate(CreateView):
    model = Extend
    form_class = PPExtendForm
    template_name = 'website/producerpageextend_form.html'

    def get_initial(self):
        initials = super(PPExtendCreate, self).get_initial()
        initials['extend_pageid'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Extended page has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('producerpage_detail', kwargs={'pk': pk})

#Resource create
class ResourceCreate(CreateView):
    model = aResource
    form_class = aResourceForm
    template_name = 'website/resource_form.html'

    def get_initial(self):
        initials = super(ResourceCreate, self).get_initial()
        initials['functional_group'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Resource has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        fg = self.kwargs['fg']
        return reverse('resource_detail', kwargs={'fg': fg})

#Resource item create
class ResourceItemCreate(CreateView):
    model = aResourceItem
    form_class = aResourceItemForm
    template_name = 'website/resourceitem_form.html'

    def get_initial(self):
        initials = super(ResourceItemCreate, self).get_initial()
        initials['resource_id'] = self.kwargs['fg']
        return initials

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request,'Resource item  has been successfully created!')
        return redirect(self.object)

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('resourceitem_detail', kwargs={'pk': pk})

#-------All Update Views below--------#
#producer home group parallax image UpdateView
class PHgPiUpdate(UpdateView):
    model = HomeGroupParallaxImage
    form_class = PHgPiForm
    template_name = 'website/phgpi_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Parallax section update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)



#producer home group text update
class PHgTextUpdate(UpdateView):
    model = HomeGroupText
    form_class = PHgTextForm
    template_name = 'website/phgtext_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Text update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)

#producer home group topic update
class HgtopicsUpdate(UpdateView):
    model = HomeGroupTopic
    form_class = HomeGroupTopicForm
    template_name = 'website/homegrouptopic_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Topic update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)


#producer page UpdateView
class PPageUpdate(UpdateView):
    model = Page
    form_class = PPageForm
    template_name = 'website/producerpage_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Page update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)

#producer page team name update
class TeamNameUpdate(UpdateView):
    model = TeamName
    form_class = TeamNameForm
    template_name = 'website/producerpageteam_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Page team name update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('producerpage_detail', kwargs={'pk': pk})

#producer page team member update
class TeamMemberUpdate(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'website/producerpageteammember_update.html'
    

#producer page extend update
class PPExtendUpdate(UpdateView):
    model = Extend
    form_class = PPExtendForm
    template_name = 'website/producerpageextend_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Extended page update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)

    def get_context_data(self, **kwargs):
        context = super(PPExtendUpdate, self).get_context_data(**kwargs)
        context['page_objects'] = Page.objects.filter(pk = self.kwargs['pk'])[:1]
        return context

#Resource update
class ResourceUpdate(UpdateView):
    model = aResource
    form_class = aResourceForm
    template_name = 'website/resource_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Resource update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('resource_detail', kwargs={'pk': pk})

#Resource update
class ResourceItemUpdate(UpdateView):
    model = aResourceItem
    form_class = aResourceItemForm
    template_name = 'website/resourceitem_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = False
        self.object.is_verified = False
        self.object.save()
        messages.success(self.request,'Resource item update is successful. Please raise a change request ticket, so that this item is verified and published')
        return redirect(self.object)
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('resourceitem_detail', kwargs={'pk': pk})


#producer page team member Delete
class TeamMemberDelete(DeleteView):
    model = TeamMember
    template_name = 'website/producerpageteammember_delete.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('producerpage_detail', kwargs={'pk': pk})



#-----Other Public Views-------#
#English Homepage
def english_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='English')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('-created', 'firstname',)
    return render(request, ['website/index_eng.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html', 'website/bcpublicpage.html', 'static/bcpublicpage.html', 'static/rightmenu.html',], {'hgmall':hgmall, 'pms':pms, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'menus': menus, 'uprofile': uprofile, })


#Chinese Homepage cn _ is for translate
def chinese_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='Chinese')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='Chinese', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='Chinese', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='Chinese', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    cnmenus = Page.objects.filter(functional_group='Chinese', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, ['website/index_chi.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html'], {'hgmall':hgmall, 'pms':pms, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'cnmenus': cnmenus, 'menus': menus, 'uprofile': uprofile, })


#Hokkien Homepage hk _ is for translate
def hokkien_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='Hokkien')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='Hokkien', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='Hokkien', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='Hokkien', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    hkmenus = Page.objects.filter(functional_group='Hokkien', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, ['website/index_hok.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html'], {'hgmall':hgmall, 'pms':pms, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'hkmenus': hkmenus, 'menus': menus, 'uprofile': uprofile,})

#Cantonese Homepage ct _ is for translate
def cantonese_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='Cantonese')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='Cantonese', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='Cantonese', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='Cantonese', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    ctmenus = Page.objects.filter(functional_group='Cantonese', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, ['website/index_can.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html'], {'hgmall':hgmall, 'pms':pms, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'ctmenus': ctmenus, 'menus': menus, 'uprofile': uprofile, })

#Indian Homepage in _ is for translate
def indian_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='Indian')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='Indian', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='Indian', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='Indian', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    inmenus = Page.objects.filter(functional_group='Indian', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, ['website/index_ind.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html'], {'hgmall':hgmall, 'pms':pms, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'inmenus': inmenus, 'menus': menus, 'uprofile': uprofile,})

#Filipino Homepage fp _ is for translate
def filipino_home(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct()
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct()
    hgms = HomeGroupManager.objects.filter(hgp_functional_group='Filipino')
    hgpis = HomeGroupParallaxImage.objects.filter(functional_group='Filipino', is_published='True', is_verified='True',)
    hgtopics = HomeGroupTopic.objects.filter(functional_group='Filipino', is_published='True', is_verified='True',)
    hgtexts = HomeGroupText.objects.filter(functional_group='Filipino', is_published='True', is_verified='True',)
    enmenus = Page.objects.filter(functional_group='English', is_published='True', is_verified='True',)
    fpmenus = Page.objects.filter(functional_group='Filipino', is_published='True', is_verified='True',)
    menus = Page.objects.filter(functional_group='All', is_published='True', is_verified='True',)
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, ['website/index_fil.html', 'static/private_menu.html', 'static/public_menu.html', 'static/simple_private_menu.html', 'static/simple_public_menu.html', 'static/base.html'], {'hgmall':hgmall, 'hgms': hgms, 'hgpis': hgpis, 'hgtopics': hgtopics, 'hgtexts': hgtexts, 'enmenus': enmenus, 'fpmenus': fpmenus, 'menus': menus, 'uprofile': uprofile, })


def none(request):
    return render(request, 'website/error.html',)


def producer(request):
    phgms = HomeGroupManager.objects.all() #producer home group managers
    phgtopics = HomeGroupTopic.objects.all() #producer home group topics
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, 'website/producer.html', {'phgms': phgms, 'phgtopics':phgtopics, 'uprofile': uprofile, })

#producer community view all link page
def producercommunity(request):
    phgms = HomeGroupManager.objects.all() #producer home group managers
    phgtopics = HomeGroupTopic.objects.all() #producer home group topics
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, 'website/producercommunity.html', {'phgms': phgms, 'phgtopics':phgtopics, 'uprofile': uprofile, })

#success return reverse url
def success(request):
    return render(request, 'website/success.html',)

#Apps Homepage
def apps(request):
    hgmall = HomeGroupManager.objects.all().values('hgp_manager_name').distinct() #homegroup managers
    pms = ProfileManager.objects.all().values('pm_manager_name').distinct() #profile managers
    stas = HelpDeskManager.objects.all().values('hdmgr_ticket_manager_name').distinct() #support ticket admins
    uprofile = UserProfile.objects.order_by('firstname', '-created',)
    return render(request, 'apps.html', {'hgmall': hgmall, 'pms': pms, 'stas': stas, 'uprofile': uprofile, })

#Apps Store
class AppsView(ListView):
    context_object_name = 'user_list'
    template_name ='apps.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AppsView, self).get_context_data(**kwargs)
        context['hgmall'] = HomeGroupManager.objects.all().filter(hgp_manager_name = self.request.user).distinct() #homegroup managers
        context['pms'] = ProfileManager.objects.all().filter(pm_manager_name = self.request.user).distinct() #profile managers
        context['ups'] = UserProfile.objects.filter(user = self.request.user).distinct() #get current user profile
        context['ups_today'] = UserProfile.objects.filter(created__gte = today)
        context['stas'] = HelpDeskManager.objects.filter(hdmgr_ticket_manager_name = self.request.user).distinct() #support ticket admins
        context['ticket_list'] = Ticket.objects.filter(first_create_date__gte = last31day) 
        context['usertickets_change'] = Ticket.objects.filter(last_modified_date__gte = today)
        context['reply24'] = Ticket.objects.filter(last_modified_date__gte = yesterday ) 
        context['usertickets_last1day'] = TicketManager.objects.filter(last_modified_date__gte = yesterday )
        context['usertickets_last7day'] = TicketManager.objects.filter(last_modified_date__gte = last7day )
        context['uprofile'] = UserProfile.objects.order_by('firstname', '-created',)
        return context  
  

#messenger
@login_required
def compose(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ComposeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save(sender=request.user)
            messages.info(request, _(u"Message successfully sent."))
            if success_url is None:
                success_url = reverse('messages_inbox')
            if 'next' in request.GET:
                success_url = request.GET['next']
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ComposeForm()
        
    return render(request, 'rightmenu_compose.html', {'form': form})




#arduino project for IOT
def iot_home(request):
    arduinoSerialData = serial.Serial('com4', 9600) #creating an object to read serial data
    measuringRod = cylinder(length=6, color=color.yellow, radius=.1, pos=(-3,-2,0))
    lengthLabel = label(text = 'Target Distance is: ', pos=(0,2,0), height=15, box=false)
    target = box(color=color.green, length=.2, width=3, height=3, pos=(0,-.5,0))

    while (1==1): #loop forever
        rate(20)

        if(arduinoSerialData.inWaiting()>0): #check to see if data is there on serial port
            myData = arduinoSerialData.readline() #if data is there, then read it.
            distance = float(myData) #Converting string myData to floating point
            myLabel = 'distance in inch: ' + myData
            return render(request, 'iot.html', {'distance': distance, 'myData': myData, 'myLabel': myLabel}) 
            

            #myLabel = 
            #lengthLabel.text = myLabel
            #target.pos=(-3+distance,-.5,0)
            #measuringRod.length = distance 






