from django.contrib import admin
from albums.models import Album
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'approved_albums']


admin.site.register(Artist, ArtistAdmin)
