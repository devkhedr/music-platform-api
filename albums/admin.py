from django.contrib import admin
from .models import Album, Song
from django import forms

class CustomizeAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('',)
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit',
        }


class InlineSong(admin.StackedInline):
    model = Song
    extra = 0
    min_num = 1
    
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'songs_count', 'is_approved']
    fields = ['name', 'artist', 'created_at', 'release_date', 'cost', 'is_approved']
    readonly_fields = ["created_at"]
    form = CustomizeAlbumForm
    inlines = [InlineSong]

admin.site.register(Album, AlbumAdmin)