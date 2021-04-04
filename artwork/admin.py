from django.contrib import admin
from .models import Artwork, SearchParam

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

class SearchParamAdmin(admin.ModelAdmin):
    list_display = ('searchName', 'user')

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(SearchParam, SearchParamAdmin)

