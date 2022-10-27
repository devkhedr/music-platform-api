from re import L
from venv import create
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewAlbumForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


class AlbumPage(View):
    def get(self, request):
        return HttpResponse('this is albums app')


@method_decorator(login_required, name='dispatch')
class CreateAlbum(View):
    def get(self, request):
        form = NewAlbumForm()
        return render(request, 'create_album.html', {'form': form})

    def post(self, request):
        form = NewAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
        return render(request, 'create_artist.html', {'form': form})
