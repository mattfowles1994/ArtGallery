from django.http import HttpResponse
from django.shortcuts import render
from artwork.models import Artwork

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    queryset = Artwork.objects.all()

    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [
            1,
            3,
            4
        ],
        "object_list": queryset
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello Contacts</h1>")
