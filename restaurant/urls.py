## quotes/urls.py
## description: URL patterns for the quotes app
## Always write a header comment
from django.urls import path

from .views import *

urlpatterns = [
    path('', main_view),
    path('main/', main_view, name='main'),
    path('order/', order_view, name='order'),
    path('confirmation/', confirmation_view, name='confirmation'),
]