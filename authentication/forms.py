from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class sign_up_form(UserCreationForm):
    email = forms.CharField(
        max_length=255, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
