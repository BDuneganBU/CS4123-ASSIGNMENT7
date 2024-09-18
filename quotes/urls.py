## quotes/urls.py
## description: URL patterns for the quotes app
## Always write a header comment
from django.urls import path

from .views import *

urlpatterns = [
    path('', base_page_view),
    path('quote/', quote_page_view),
    path('show_all/', showall_page_view),
    path('about/', about_page_view),
]