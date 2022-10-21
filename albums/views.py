from re import L
from venv import create
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import new_album_form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


class album_page(View):
    def get(self, request):
        return HttpResponse('this is albums app')


@method_decorator(login_required, name='dispatch')
class create_album(View):
    def get(self, request):
        form = new_album_form()
        return render(request, 'create_album.html', {'form': form})

    def post(self, request):
        form = new_album_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
        return render(request, 'create_artist.html', {'form': form})
