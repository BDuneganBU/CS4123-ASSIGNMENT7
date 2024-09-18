## quotes/models.py
## description: Model patterns for the quotes app
## Always write a header comment

from django.db import models

# Create your models here.
class Post(models.Model):
    banner = models.ImageField(blank=True)