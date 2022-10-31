from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('artists/', views.ArtistsList.as_view(), name='artist_page'),
    path('artists/create/', views.CreateArtist.as_view(), name='create_artist'),
]
