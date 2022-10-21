from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('artists/', views.artist_page.as_view(), name='artist_page'),
    path('artists/create/', views.create_artist.as_view(), name='create_artist'),
]
