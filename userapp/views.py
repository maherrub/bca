from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.http import HttpRequest 
from django.shortcuts import render, redirect
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
from django.db.models import Q

#userapp imports
from userapp.models import *
from userapp.forms import *
from userapp.choices import *

#website imports
from website.choices import *
from website.validators import *

#django-messages imports
from django_messages.models import *
from django_messages.forms import *


#definitions
app_name = 'userapp'



# Create your views here.
# Main views below ListView, DetailView, CreateView, UpdateView

class UpList(ListView):

    model = UserProfile
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super(UpList, self).get_context_data(**kwargs)
        context['uprofile']  = UserProfile.objects.order_by('-created', 'firstname',)    
        return context

    def dispatch(self, *args, **kwargs):
        return super(UpList, self).dispatch(*args, **kwargs)

class UpDetail(DetailView):

    model = UserProfile

    def dispatch(self, *args, **kwargs):
        return super(UpDetail, self).dispatch(*args, **kwargs)


#-------All Create Views below--------#
class UpCreate(CreateView):

    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userapp/userprofile_form.html'


    def dispatch(self, *args, **kwargs):
        return super(UpCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request,'Your profile has been successfully created!')
        return redirect(self.object)


class UpUpdate(UpdateView):

    model = UserProfile
    form_class = UserProfileForm
    template_name_suffix = '_update'

    def dispatch(self, *args, **kwargs):
        return super(UpUpdate, self).dispatch(*args, **kwargs)

#profile managers user profile update
class PMUPUpdate(UpdateView):
    model = UserProfile
    form_class = PMUPForm
    template_name = 'userapp/profilemanager_update.html'


#profile manage's List view
class PMUpList(ListView):
    model = UserProfile
    template_name = 'userapp/profilemanager_list.html'
    paginate_by = 20

          
    def get_queryset(self, **kwargs):
        qs = super(PMUpList, self).get_queryset(**kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(user__username__icontains=query)|
                Q(user__email__icontains=query)|
                Q(usermobile__contains=query)|
                Q(firstname__icontains=query)|
                Q(lastname__icontains=query)|
                Q(address_line1__icontains=query)|
                Q(address_line2__icontains=query)|
                Q(city_or_town__icontains=query)|
                Q(postal_code__contains=query)|
                Q(dob__contains=query)|
                Q(who_brought_you_here__icontains=query)|
                Q(whos_mobile_number__contains=query)|
                Q(created__contains=query)
                ).distinct()


        return qs.filter(sunday_service__exact=self.kwargs['fg'])

    
    

#profile manager's console
def PMCView(request):
    ups = UserProfile.objects.all()
    pms = ProfileManager.objects.all()
    return render(request,'userapp/profilemanager.html', {'ups':ups, 'pms':pms,})


#social media user list
class SocialMediaUserList(ListView):
    model = UserProfile
    template_name = 'userapp/socialmediauser_list.html'

    paginate_by = 20

          
    def get_queryset(self, **kwargs):
        qs = super(SocialMediaUserList, self).get_queryset(**kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(user__username__icontains=query)|
                Q(user__email__icontains=query)|
                Q(usermobile__contains=query)|
                Q(firstname__icontains=query)|
                Q(lastname__icontains=query)|
                Q(address_line1__icontains=query)|
                Q(address_line2__icontains=query)|
                Q(city_or_town__icontains=query)|
                Q(postal_code__contains=query)|
                Q(dob__contains=query)|
                Q(who_brought_you_here__icontains=query)|
                Q(whos_mobile_number__contains=query)|
                Q(created__contains=query)
                ).distinct()


        return qs.filter(country=self.kwargs['fg'])

#friend requests

#class FriendRequestCreate(CreateView):
#    model = FriendsList
#    form_class = FriendRequestForm
#    template = 'userapp/socialmediauser_list.html'




