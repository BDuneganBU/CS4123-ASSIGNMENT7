## Create app-specific URL:
# mini_fb/urls.py
from django.urls import path
from . import views
urlpatterns = [
    # map the URL (empty string) to the view
    path('', views.ShowAllProfilesView.as_view(), name='show_all'), # generic class-based view
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
]