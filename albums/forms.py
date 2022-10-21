from django import forms
from .models import album



class new_album_form(forms.ModelForm):
    class Meta:
        model = album
        fields = ['album_name', 'album_artist', 'released_at', 'price', 'is_approved']
        widgets = {
            'released_at':forms.TextInput(attrs={'type':'datetime-local'}),
        }