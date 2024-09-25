from django.shortcuts import render, redirect

# Create your views here.

def show_form(request):
    '''Show contact form'''
    template_name = "formdata/form.html"
    return render(request, template_name)

def submit(request):
    '''Submit form data --Always put doc strings for extra points!'''
    template_name = 'formdata/confirmation.html'
    #read form data
    if (request.POST):
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']
    
    #condense into context for template
        context = {'name': name,
                    'favorite_color': favorite_color}

        return render(request, template_name, context)
    
    #Graceful handling of going straight to submit directory
    return redirect('show_form')

