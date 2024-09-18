######## pages/urls.py ########
# description: direct URL requests to views

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView),
] 