from django.contrib import admin
from .models import Artwork, SearchParam, Enquiry

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

class SearchParamAdmin(admin.ModelAdmin):
    list_display = ('searchName', 'user')

class EnquiryParamAdmin(admin.ModelAdmin):
    list_display = ('userid', 'artworkname', 'staffusername')

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(SearchParam, SearchParamAdmin)
admin.site.register(Enquiry, EnquiryParamAdmin)

