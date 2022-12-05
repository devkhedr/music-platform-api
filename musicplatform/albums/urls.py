from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.AlbumPage.as_view({
       'post': 'create'    
    }), name='album_page'),
    path('albums/manual/',views.AlbumPageManual.as_view(),name="albums_manual"),
    path('albums/create/', views.CreateAlbum.as_view(), name='create_album'),
]