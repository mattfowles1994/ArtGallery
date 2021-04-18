from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from artwork.models import Artwork, SearchParam, New
from .forms import FilterForm
from django.db.models import Q

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    queryset = Artwork.objects.all()
    news = New.objects.filter(active=1).first()
    searchset = SearchParam.objects.all().filter(user=request.user.id)
    #print(request.session)
    if 'search' in request.session:
        currentSearch = request.session['search']
        print(currentSearch)
        currentSearch = SearchParam.objects.all().filter(id=currentSearch)
        try:
            form = FilterForm(request.POST or None, initial={
                "searchName": currentSearch[0].searchName,
                "title": currentSearch[0].title,
                "price": currentSearch[0].price,
                "width": currentSearch[0].width,
                "height": currentSearch[0].height,
                "artist": currentSearch[0].artist,
                "year": currentSearch[0].year
                })
            if currentSearch[0].title is not None:
                queryset = queryset.filter(title__startswith=currentSearch[0].title)
            if currentSearch[0].price is not None:
                queryset = queryset.filter(price__lte=currentSearch[0].price)
            if currentSearch[0].width is not None:
                queryset = queryset.filter(width__lte=currentSearch[0].width)    
            if currentSearch[0].height is not None:
                queryset = queryset.filter(height__lte=currentSearch[0].height)
            if currentSearch[0].artist is not None:
                queryset = queryset.filter(artist__startswith=currentSearch[0].artist)
            if currentSearch[0].year is not None:
                queryset = queryset.filter(year__gte=currentSearch[0].year)
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
                del request.session['search']
                return redirect('home')
        if 'search' in request.POST:
            form = FilterForm(request.POST)
            searchId = request.POST['old_search']
            request.session['search'] = searchId
            return redirect('home')
        if 'reset' in request.POST:
            form = FilterForm(request.POST)
            if 'search' in request.session:
                del request.session['search']
            queryset = Artwork.objects.all()

    my_context = {
        "object_list": queryset,
        "form" : form,
        "search_list": searchset,
        "news" : news
    }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    context = {
    
    }
    return render(request, "about.html", context)
