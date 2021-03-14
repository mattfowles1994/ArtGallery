from django.contrib import admin
from .models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
admin.site.register(Artwork, ArtworkAdmin)