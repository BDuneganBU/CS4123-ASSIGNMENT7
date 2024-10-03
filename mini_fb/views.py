## Create View
# mini_fb/views.py
# Define the views for the mini_fb app:
#from django.shortcuts import render
from .models import *
from django.views.generic import ListView #ListView is a custom component which displays a list of the model

#class-based view
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all mini_fb articles.'''
    model = Profile # retrieve objects of type Article from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file (context variable)