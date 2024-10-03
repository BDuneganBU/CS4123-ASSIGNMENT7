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