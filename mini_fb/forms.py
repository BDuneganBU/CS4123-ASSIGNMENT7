# mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to add a Profile to the database.'''
    class Meta:
        '''associate this form with the Comment model; select fields'''
        model = Profile #relate to the Profile Model
        fields = ['firstName', 'lastName', 'city','email', 'profileImageURL']  # which fields from model should we use

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to add a status message for a profile to the database'''
    class Meta:
        model = StatusMessage
        fields = ['message']  # which fields from model should we use