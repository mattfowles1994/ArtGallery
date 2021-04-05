from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from artwork.models import Artwork, SearchParam
from .forms import FilterForm

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    queryset = Artwork.objects.all()
    searchset = SearchParam.objects.all().filter(user=request.user.id)
    #print(request.session)
    if 'search' in request.session:
        try:
            currentSearch = request.session['search']
            currentSearch = SearchParam.objects.all().filter(id=currentSearch)
            form = FilterForm(request.POST or None, initial={
                "searchName": currentSearch[0].searchName,
                "title": currentSearch[0].title,
                "price": currentSearch[0].price,
                "width": currentSearch[0].width,
                "height": currentSearch[0].height,
                "artist": currentSearch[0].artist,
                "year": currentSearch[0].year
                })
        except:
            form = FilterForm(request.POST or None)
        
    else:
        form = FilterForm(request.POST or None)

    if request.method == 'POST':
        if 'save' in request.POST:
            form = FilterForm(request.POST)
            if form.is_valid():
                search = form.save()
                search.user = request.user.id

                try:
                    delete = SearchParam.objects.all().filter(user=search.user, searchName=search.searchName).delete()
                    search.save()
                except:
                    search.save()

                search = SearchParam.objects.all().filter(user=search.user, searchName=search.searchName).values_list('id', flat=True)
                request.session['search'] = search[0]
                return redirect('home')

        if 'delete' in request.POST: 
            form = FilterForm(request.POST)
            print(form.fields['searchName'])
            if form.is_valid():
                print(form.fields['searchName'])
                search = form.save()
                delete = SearchParam.objects.all().filter(user=request.user.id, searchName=search.searchName).delete()
                request.session['search'] = 0
                return redirect('home')
        if 'search' in request.POST:
            form = FilterForm(request.POST)
            searchId = request.POST['old_search']
            request.session['search'] = searchId
            return redirect('home')

    my_context = {
        "object_list": queryset,
        "form" : form,
        "search_list": searchset,
        "current_search": currentSearch
    }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    context = {
    
    }
    return render(request, "about.html", context)
