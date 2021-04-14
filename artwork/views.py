from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Artwork
from .forms import ArtworkForm, RawArtForm, EnquiryForm

# function based views

# Create your views here.
def dynamic_lookup_view(request, id):
    try:
        obj = Artwork.objects.get(id=id)
        try:
            enq = Enquiry.objects.get.filter(userid=request.user, artworkname=obj.title)
        except:
            enq = None
    except Artwork.DoesNotExist:
        raise Http404

    form = EnquiryForm(request.POST or None)

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            enquiry.userid = request.user
            enquiry.artworkname = obj.title
            enquiry.save()
            return redirect(obj)

    context = {
        'object':obj,
        "form" : form,
        "enq" :enq
    }
    return render(request, "artwork/detail.html", context)


def artwork_list_view(request):
    queryset = Artwork.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, "artwork/list.html", context)