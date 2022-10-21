from django.shortcuts import redirect, render
from .models import artist
from .forms import new_artist_form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


class home(View):
    def get(self, request):
        return render(request, 'home.html')


class artist_page(View):
    def get(self, request):
        artists_list = artist.objects.all()
        return render(request, 'artists.html', {'artists_list': artists_list})


@method_decorator(login_required, name='dispatch')
class create_artist(View):
    def post(self, request):
        form = new_artist_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
        return render(request, 'create_artist.html', {'form': form})
    
    def get(self, request):
        form = new_artist_form()
        return render(request, 'create_artist.html', {'form': form})