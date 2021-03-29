from django.http import HttpResponse
from django.shortcuts import render
from artwork.models import Artwork
from .forms import FilterForm

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    queryset = Artwork.objects.all()

    form = FilterForm(request.POST or None)
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            SearchParam.objects.create()
            return redirect('home')

    my_context = {
        "object_list": queryset,
        "form" : form
    }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    context = {
    
    }
    return render(request, "about.html", context)
