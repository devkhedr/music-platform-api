from django import forms
from .models import Album



class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'release_date', 'cost', 'is_approved']
        widgets = {
            'release_date':forms.TextInput(attrs={'type':'datetime-local'}),
        }