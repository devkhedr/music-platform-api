from re import L
from venv import create
from django.shortcuts import redirect, render
from .forms import NewAlbumForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .serializers import AlbumSerializer
from rest_framework import status, permissions, pagination, viewsets, generics
from .models import Album
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django_filters import rest_framework as filters
import sys
from .tasks import send_email_for_new_album


class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'cost': ['gte', 'lte'],
            'name': ['icontains'],
        }


class AlbumPage(viewsets.ModelViewSet):
    queryset = Album.objects.filter(is_approved=True)
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = AlbumFilter

    @permission_classes([permissions.AllowAny])
    def get(self, request):
        albums = Album.objects.filter(is_approved=True)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)

    @permission_classes([permissions.IsAuthenticated])
    def create(self, request):
        if not hasattr(request.user, 'artist'):
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'message': 'You must be an artist to create an album'})
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_email_for_new_album(
            serializer.data['name'], serializer.data['artist']["id"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlbumPageManual(generics.ListAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = AlbumFilter

    def get(self, request, *args, **kwargs):
        params = request.query_params
        gte, lte, icontains = 0, sys.maxsize, ''
        if 'cost__gte' in params:
            if params['cost__gte']:
                try:
                    data = int(params['cost__gte'])
                    gte = data
                except:
                    return Response(data={"cost__gte": ["Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)

        if 'cost__lte' in params:
            if params['cost__lte']:
                try:
                    data = int(params['cost__lte'])
                    lte = data
                except:
                    return Response(data={"cost__lte": ["Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)

        if 'name__icontains' in params:
            if params['name__icontains']:
                icontains = params['name__icontains']

        data = Album.objects.filter(
            cost__gte=gte, cost__lte=lte, name__icontains=icontains)
        serializer = AlbumSerializer(data, many=True)

        if 'limit' not in params:
            return Response(serializer.data)

        return self.get_paginated_response(self.paginate_queryset(serializer.data))


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
