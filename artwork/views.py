from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Artwork
from .forms import ArtworkForm, RawArtForm

# function based views

# Create your views here.
def artwork_detail_view(request):
    obj = Artwork.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "artwork/detail.html", context)

def artwork_create_view(request):
#    initial_data = {
#        'title':'this is a cool title'
#    }
    obj = Artwork.objects.get(id=1)

    form = ArtworkForm(request.POST or None, instance=obj)
    if request.method == "POST":
        form = ArtworkForm(request.POST)
        if form.is_valid():
            Artwork.objects.create(**form.cleaned_data)
            form = ArtworkForm()

    context = {
        'form': form
    }
    return render(request, "artwork/create.html", context)

#    form = ArtworkForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ArtworkForm()
#
#    context = {
#        'form': form
#    }
#    return render(request, "artwork/create.html", context)

def dynamic_lookup_view(request, id):
    #obj = Artwork.objects.get(id=id)

    #obj = get_object_or_404(Artwork, id=id)

    try:
        obj = Artwork.objects.get(id=id)
    except Artwork.DoesNotExist:
        raise Http404

    context = {
        'object':obj
    }
    return render(request, "artwork/detail.html", context)

def artwork_delete_view(request, id):
    obj = get_object_or_404(Artwork, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }

    return render(request, "artwork/delete.html", context)

def artwork_list_view(request):
    queryset = Artwork.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, "artwork/list.html", context)