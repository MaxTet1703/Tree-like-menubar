from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")

def menu_topic(request, url):
    return render(request, "home.html")