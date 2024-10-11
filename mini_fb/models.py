## Create a Model 
#
# mini_fb/models.py
# Define the data objects for our application
#
from django.db import models

#Each model is a class
class Profile(models.Model): #class MUST inheirit 
    '''Encapsulate the idea of an Profile by some author.'''
    # data attributes of an Profile:
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    profileImageURL = models.URLField(blank=True)
    
    #Default method so name MUST match (Admin can display this rather than the unique ID)
    def __str__(self):
        '''Return a string representation of this Profile object.'''
        return f'{self.firstName} {self.lastName}'
    
    def get_statusMessages(self):
        '''Return all of the statusMessages about this profile.'''
        messages = StatusMessage.objects.filter(profile=self)
        return messages

class StatusMessage(models.Model):
    '''Encapsulate the idea of a status message for some profile.'''
    #each StatusMessage has a ForeignKey of type Profile creating a many-to-one relationship
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    #timestamp defaults to the current system time
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)

    def __str__(self):
        '''Return a string representation of this StatusMessage object.'''
        return f'{self.message}'