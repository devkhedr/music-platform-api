from django.contrib import admin
from albums.models import album
from .models import artist


class artist_admin(admin.ModelAdmin):
    list_display = ['stage_name', 'approved_albums']


admin.site.register(artist, artist_admin)
