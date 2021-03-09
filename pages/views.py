from django.http import HttpResponse
from django.shortcuts import render
from artwork.models import Artwork

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    queryset = Artwork.objects.all()

    my_context = {
        "object_list": queryset
    }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    context = {
    
    }
    return render(request, "about.html", context)
