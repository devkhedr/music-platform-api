from datetime import datetime
from decimal import Decimal
import pytest
from albums.models import Album
from albums.serializers import AlbumSerializer
from artists.models import Artist
from dateutil.parser import parse
from users.models import CustomUser


@pytest.mark.django_db
def test_serializer_returns_expected_fields_and_data():
    user = CustomUser.objects.create_user(username='user')
    artist = Artist.objects.create(user=user, stage_name='artist')
    album = Album.objects.create(
        artist=artist, name='album', release_date=datetime(2022, 10, 10), cost=100.10)

    serializer = AlbumSerializer(album)

    assert serializer.data['id'] == album.id
    assert serializer.data['artist']['id'] == artist.id
    assert serializer.data['artist']['stage_name'] == artist.stage_name
    assert serializer.data['artist']['social_link'] == artist.social_link
    assert serializer.data['name'] == album.name
    assert parse(serializer.data['release_date'][:-1]) == album.release_date
    assert float(Decimal(serializer.data['cost'])) == float(
        Decimal(album.cost))


@pytest.mark.django_db
def test_serializer_with_valid_data():
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
        "cost": 100
    })

    serializer.is_valid(raise_exception=False)
    assert not serializer.errors
    assert serializer.validated_data['name'] == 'album'
    assert float(serializer.validated_data['cost']) == float(Decimal(100.00))


@pytest.mark.django_db
def test_serializer_with_missing_data():
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
    })

    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])


@pytest.mark.django_db
def test_serializer_with_wrong_data1():
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
        "cost": "string"
    })

    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])


@pytest.mark.django_db
def test_serializer_with_worng_data2():
    serializer = AlbumSerializer(data={
        "name": "album",
        "release_date": "10-5",
        "cost": 100
    })

    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['release_date'])
