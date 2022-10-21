from tkinter import Widget
from django import forms
from .models import artist


class new_artist_form(forms.ModelForm):
    class Meta:
        model = artist
        fields = ['stage_name', 'social_link']
