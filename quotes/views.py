## quotes/views.py
## description: View patterns for the quotes app
## Always write a header comment

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.
quote_list = ["The only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion.",
              "Don't walk behind me; I may not lead. Don't walk in front of me; I may not follow. Just walk beside me and be my friend.",
              "Sometimes, carrying on, just carrying on, is the superhuman achievement.",
              "In the depths of winter, I finally learned that within me there lay an invincible summer.",
              "There is no love of life without the despair of life."]
image_list = ['/media/camus1.jpg',
              '/media/camus2.jpg',
              '/media/camus3.jpg',
              '/media/camus4.jpg',
              '/media/camus5.jpg']

def base_page_view(request):
    """provides the functionality for the base page"""
    randQuoteIndex = random.randint(0,len(quote_list)-1)
    randImgIndex = random.randint(0,len(image_list)-1)
    randQuote = quote_list[randQuoteIndex]
    randImg = image_list[randImgIndex]
    context = {"quote": randQuote,
               "image": randImg}
    
    return render(request, "quotes/base.html", context)

def quote_page_view(request):
    """provides the functionality for the quote page"""
    randQuoteIndex = random.randint(0,len(quote_list)-1)
    randImgIndex = random.randint(0,len(image_list)-1)
    randQuote = quote_list[randQuoteIndex]
    randImg = image_list[randImgIndex]
    context = {"quote": randQuote,
               "image": randImg}
    return render(request, "quotes/quote.html", context)

def showall_page_view(request):
    """provides the functionality for the show_all page"""
    context = {"images" : image_list,
               "quotes": quote_list}
    return render(request, "quotes/show_all.html", context)

def about_page_view(request):
    """provides the functionality for the about page"""
    context = {"name": "Bob"}
    return render(request, "quotes/about.html", context)