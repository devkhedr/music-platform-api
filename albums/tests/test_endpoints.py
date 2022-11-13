import pytest
import pytz
from rest_framework.test import APIClient
from datetime import datetime
from decimal import Decimal
from users.models import CustomUser
from artists.models import Artist
from albums.models import Album


@pytest.mark.django_db
def test_create_album_with_missing_fileds(auth_client):
    user = CustomUser.objects.create_user(username='user')
    Artist.objects.create(user=user, stage_name='artist')

    client = auth_client(user)

    album = {
        "name": "album1",
        "cost": 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == 403


@pytest.mark.django_db
def test_create_an_album_with_unauthenticated_user():
    client = APIClient()

    album = {
        "name": "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost": 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == 403


@pytest.mark.django_db
def test_create_an_album_with_authenticated_user_who_is_not_an_artist(auth_client):
    client = auth_client()

    album = {
        "name": "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost": 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == 403
