from django.shortcuts import render

# Create your views here.


def home(request):
    """
        Rendering not expanding menu 
    """
    return render(request, "home.html")

def menu_topic(request, url):
    """
        Rendering expanding menu by url
    """
    return render(request, "home.html")