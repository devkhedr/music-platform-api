from django.shortcuts import redirect, render
from .models import Artist
from .forms import NewArtistForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ArtistsList(APIView):
    def get(self, request, *args, **kwargs):
        q = Artist.objects.all()
        serializer = ArtistSerializer(q,many=True)
        return Response(serializer.data)

    def post(self, request ,*args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@method_decorator(login_required, name='dispatch')
class CreateArtist(View):
    def post(self, request):
        form = NewArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
        return render(request, 'create_artist.html', {'form': form})
    
    def get(self, request):
        form = NewArtistForm()
        return render(request, 'create_artist.html', {'form': form})
    
    
#this is related to home page 
class Home(View):
    def get(self, request):
        return render(request, 'home.html')