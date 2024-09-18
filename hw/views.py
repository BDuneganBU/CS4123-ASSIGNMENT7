## hw/views.py
## write view functions to handle URL requests for the hw app
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random


# Create your views here.
# def home(request):
#     """Handle main URL for the hw app"""
#     x = 5

#     #This would be cooler if you could connect it to a .html file
      #Damn, I should have just waited
#     return HttpResponse("Hello, world!")
#     response_text = f'''
#         <html>
#             <h1>Hello, World!</h1>
#             <p>This is a Django app.</p>
#             This is a var: {x}
#         </html>
#     '''

#     return HttpResponse(response_text)

def home(request):
    """Handle main URL for the hw app which delegates rendering to template hw/home.html"""
    template_name = 'hw/home.html'
    #Dictionary of context variables for the template
    context = {
        "current_time" : time.ctime(),
        "letter1" : chr(random.randint(65,90))
    }
    return render(request, template_name, context)
