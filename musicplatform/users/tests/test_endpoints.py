from mmusicplatform.conftest import auth_client
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser


@pytest.mark.django_db
def test_get_correct_user():
    CustomUser.objects.create_user(
        username="MuhammedKhedr", email="m@gmail.com", password="pass123")
    client = APIClient()
    response = client.get('/users/1/')
    data = response.data

    assert response.status_code == 200
    assert data['username'] == 'MuhammedKhedr'
    assert data['email'] == 'm@gmail.com'
    assert 'bio' in data


@pytest.mark.django_db
def test_get_non_existing_user():
    client = APIClient()
    response = client.get('/users/1/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_updates_without_authentication():
    CustomUser.objects.create_user(
        username="MuhammedKhedr", email="m@gmail.com", password="pass123")

    update_user = {
        'username': 'Khedr07',
        'email': 'kkk@gmail.com',
    }

    client = APIClient()
    response = client.put('/users/1/', update_user)
    assert response.status_code == 403
