## Create a Model 
#
# blog/models.py
# Define the data objects for our application
#
from django.db import models

#Each model is a class
class Article(models.Model): #class MUST inheirit 
    '''Encapsulate the idea of an Article by some author.'''
    # data attributes of an Article:
    title = models.TextField(blank=False) #There is a bunch of optional parameters
    author = models.TextField(blank=False) #blank=False means the field is required to be filled for each Article Model
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True) #auto_now=True sets the time to now upon Model instantiation
    image_url = models.URLField(blank=True) ## new
    
    #Default method so name MUST match (Admin can display this rather than the unique ID)
    def __str__(self):
        '''Return a string representation of this Article object.'''
        return f'{self.title} by {self.author}'