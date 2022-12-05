import pytest
from artists.models import Artist
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_artist_success(auth_client):
    artist = {
        "stage_name": "MuhammedKhedr",
        "social_link": "https://www.facebook.com/khedr07",
        "user": 1
    }
    client = auth_client()
    response = client.post('/artists/', artist)
    data = response.data
    assert response.status_code == 200
    assert data['stage_name'] == 'MuhammedKhedr'
    assert data['social_link'] == 'https://www.facebook.com/khedr07'


@pytest.mark.django_db
def test_get_artists_success(auth_client):
    artist = {
        "stage_name": "MuhammedKhedr",
        "social_link": "https://www.facebook.com/khedr07",
        "user": 1
    }
    client = auth_client()
    response = client.post('/artists/', artist)
    assert response.status_code == 200
