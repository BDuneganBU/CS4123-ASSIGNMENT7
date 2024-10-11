## Create View
# mini_fb/views.py
# Define the views for the mini_fb app:
#from django.shortcuts import render
import profile

from django.forms import BaseModelForm
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import CreateProfileForm, CreateStatusMessageForm
from django.urls import reverse
from typing import Any

#class-based view
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all mini_fb articles.'''
    model = Profile # retrieve objects of type Article from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file (context variable)

#A more detailed version for a single profile
class ShowProfilePageView(DetailView):
    '''Create a class that inheirits DetailView to display a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

#The view to create a new profile
class CreateProfileView(CreateView):
    '''A view to create a new profile and save it to the database.'''
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

#The view to create a new StatusMessage
class CreateStatusMessageView(CreateView):
    '''A view to create a new StatusMessage and save it to the database.'''
    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''
        Build the dict of context data for this view.
        '''
        # superclass context data
        context = super().get_context_data(**kwargs)
        # find the pk from the URL
        pk = self.kwargs['pk']
        # find the corresponding article
        profile = Profile.objects.get(pk=pk)
        # add article to context data
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''
        Handle the form submission. We need to set the foreign key by 
        attaching the Profile to the StatusMessage object.
        We can find the article PK in the URL (self.kwargs).
        '''
        print(form.cleaned_data)
        #find Article identified by the PK from the URL pattern
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        #Attach Article to the instance of the comment set to its PK
        form.instance.profile = profile
        #Delegate work to super
        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successfully submitting form.'''
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})