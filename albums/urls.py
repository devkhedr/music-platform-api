from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.AlbumPage.as_view(), name='album_page'),
    path('albums/create/', views.CreateAlbum.as_view(), name='create_album'),
]
