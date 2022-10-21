from django.contrib import admin
from .models import album, song
from django import forms

class customize_album_form(forms.ModelForm):
    class Meta:
        model = album
        exclude = ('',)
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit',
        }


class inline_song(admin.StackedInline):
    model = song
    extra = 0
    min_num = 1
    
class album_admin(admin.ModelAdmin):
    list_display = ['album_name', 'album_artist', 'songs_count', 'is_approved']
    fields = ['album_name', 'album_artist', 'created_at', 'released_at', 'price', 'is_approved']
    readonly_fields = ["created_at"]
    form = customize_album_form
    inlines = [inline_song]

admin.site.register(album, album_admin)