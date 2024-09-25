## restaurant/views.py
## description: View patterns for the restaurant app
## Always write a header comment

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import datetime
import random


daily_special = ['Schnitzel',
              'Schweinshaxen',
              'Blaukraut Salat',
              'Sauerkraut Salat',
              'Leberkase']
              
special_costs = ['$15.99',
                 '$22.99',
                 '$7.99',
                 '$7.99',
                 '$10.99']



# Create your views here.

def main_view(request):
    """provides the functionality for the main page"""
    context = {}
    return render(request, "restaurant/main.html", context)

def order_view(request):
    """provides the functionality for the order page"""
    randSpecialIndex = random.randint(0,len(daily_special)-1)
    randSpecial = daily_special[randSpecialIndex]
    randCost = special_costs[randSpecialIndex]
    context = {"special_item": randSpecial,
               "special_cost": randCost}
    return render(request, "restaurant/order.html", context)

def confirmation_view(request):
    """provides the functionality for the confirmation page"""
    #Store the items that were ordered
    template_name = 'formdata/confirmation.html'
    total_cost = 0.0
    ordered = []
    #read form data
    if (request.POST):
        meal1 = request.POST.get('meal1', '')
        side1 = request.POST.get('side1', '')

        meal2 = request.POST.get('meal2', '')
        side2 = request.POST.get('side2', '')

        meal3 = request.POST.get('meal3', '')
        side3 = request.POST.get('side3', '')

        meal4 = request.POST.get('meal4', '')
        side4 = request.POST.get('side4', '')

        spz = request.POST.get('spz', '')
        special_item = request.POST['special_item']
        special_cost = request.POST['special_cost']

        instructions = request.POST.get('instructions', 'None')

        name = request.POST.get('name', 'John Doe')
        if(name == ''):
            name = 'John Doe'
        phone = request.POST.get('phone', 'XXX-XXX-XXXX')
        if(phone == ''):
            phone = 'XXX-XXX-XXXX'
        email = request.POST.get('email', 'johndoe@gmail.com')
        if(email == ''):
            email = 'johndoe@gmail.com'
    
        if(meal1 == 'on'):
            total_cost += 10.99
            addition = "Meal 1"
            if(side1 == 'Sauerkraut'):
                addition += " with Side Sauerkraut"
            elif(side1 == 'Potato'):
                addition += " with Side Potato Salad"
            else:
                addition += " with no side"
            ordered.append(addition)

        if(meal2 == 'on'):
            total_cost += 12.99
            addition = "Meal 2"
            if(side2 == 'Sauerkraut'):
                addition += " with Side Sauerkraut"
            elif(side2 == 'Potato'):
                addition += " with Side Potato Salad"
            else:
                addition += " with no side"
            ordered.append(addition)

        if(meal3 == 'on'):
            total_cost += 11.99
            addition = "Meal 3"
            if(side3 == 'Sauerkraut'):
                addition += " with Side Sauerkraut"
            elif(side3 == 'Potato'):
                addition += " with Side Potato Salad"
            else:
                addition += " with no side"
            ordered.append(addition)

        if(meal4 == 'on'):
            total_cost += 13.99
            addition = "Meal 4"
            if(side4 == 'Sauerkraut'):
                addition += " with Side Sauerkraut"
            elif(side4 == 'Potato'):
                addition += " with Side Potato Salad"
            else:
                addition += " with no side"
            ordered.append(addition)

        if(spz == 'on'):
            total_cost += float(special_cost[1:])
            ordered.append(special_item)


        #Create a random readyTime (30-60min)
        expected = readyTime()
        expected = expected.strftime("%H:%M")

        context = {'ordered': ordered,
                'instructions': instructions,
                'name':name,
                'phone':phone,
                'email':email,
                'total_cost':total_cost,
                'expected': expected}
        return render(request, "restaurant/confirmation.html", context)
    
    return redirect('order')

def readyTime():
    current_time = datetime.datetime.now()
    rand_min = random.randint(30, 60)
    expected = current_time + datetime.timedelta(minutes=rand_min)
    return expected
