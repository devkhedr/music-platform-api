from tkinter import Widget
from django import forms
from .models import Artist


class NewArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stage_name', 'social_link']
