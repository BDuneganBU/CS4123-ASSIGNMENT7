######## file: pages/views.py ########
# description: provide a view to send to the user

from django.shortcuts import render

# Create your views here.
def HomePageView(request):
    return render(request, "pages/home.html")