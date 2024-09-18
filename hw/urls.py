## hw/urls.py
## description: URL patterns for the hw app
## Always write a header comment

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.home, name="home"),
    
]