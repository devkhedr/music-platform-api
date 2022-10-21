from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_page.as_view(), name='album_page'),
    path('albums/create/', views.create_album.as_view(), name='create_album'),
]
