from django.contrib import admin
from albums.models import album
from .models import artist


class inline_album(admin.StackedInline):
    model = album
    extra = 1


class artist_admin(admin.ModelAdmin):
    list_display = ['stage_name', 'approved_albums']
    inlines = [inline_album]


admin.site.register(artist, artist_admin)
