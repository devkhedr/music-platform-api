from django import forms
from .models import Album



class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'album_artist', 'released_at', 'price', 'is_approved']
        widgets = {
            'released_at':forms.TextInput(attrs={'type':'datetime-local'}),
        }