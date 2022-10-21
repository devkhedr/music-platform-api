from django.contrib import admin
from .models import album


class album_admin(admin.ModelAdmin):
    list_display = ['album_name', 'album_artist', 'is_approved']
    readonly_fields = ["album_creation_date"]


admin.site.register(album, album_admin)
