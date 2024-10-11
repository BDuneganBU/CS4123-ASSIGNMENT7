## Create View
# mini_fb/views.py
# Define the views for the mini_fb app:
#from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

#class-based view
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all mini_fb articles.'''
    model = Profile # retrieve objects of type Article from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file (context variable)

class ShowProfilePageView(DetailView):
    '''Create a class that inheirits DetailView to display a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'