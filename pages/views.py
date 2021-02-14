from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    my_context = {
        "title": "badass brews and beds",
    }
    return render(request, "home.html", my_context)

def menu_view(request, *args, **kwargs):
    return render(request, "menu.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number" : 23,
        "my_list" : [55, 77, 99]
    }
    return render(request, "about.html", my_context)