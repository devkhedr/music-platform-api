import pytest
from rest_framework import status
from rest_framework.test import APIClient


################## Regiter Testing ##################
@pytest.mark.django_db
def test_register_with_correct_data():
    user = {
        'username' : "MuhammedKhedr",
        'email' : "m@mail.com",
        'password1' : "mo123456",
        'password2' : "mo123456"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)
    data = response.data

    assert response.status_code == 201
    assert data['user']['username'] == user['username']
    assert data['user']['email'] == user['email']


@pytest.mark.django_db
def test_register_with_unequal_passwords():
    user = {
        'username' : "MuhammedKhedr",
        'email' : "m@mail.com",
        'password1' : "mo123456",
        'password2' : "nkjhkhjli"
    }
    client = APIClient()
    response = client.post('/authentication/register/', user)
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_missing_password2_field():
    user = {
        'username' : "MuhammedKhedr",
        'email' : "m@mail.com",
        'password1' : "mo123456",
    }
    client = APIClient()
    response = client.post('/authentication/register/', user)
    assert response.status_code == 400



################## Login Testing ##################
@pytest.mark.django_db
def test_login_successfuly():
    user = {
        'username' : "MuhammedKhedr",
        'email' : "m@mail.com",
        'password1' : "mo123456",
        'password2' : "mo123456"
    }
    client = APIClient()
    client.post('/authentication/register/', user)
    response = client.post('/authentication/login/', {'username' : "MuhammedKhedr", 'password' : "mo123456",})
    data = response.data
    assert response.status_code == 200
    assert data['user']['username'] == user['username']


@pytest.mark.django_db
def test_with_non_exiting_user():
    client = APIClient()
    response1 = client.post('/authentication/login/', {'username' : "MuhammedKhedr", 'password' : "mo123456",})
    assert response1.status_code == 400


@pytest.mark.django_db
def test_login_with_missing_password_field():
    user = {
        'username' : "MuhammedKhedr",
        'email' : "m@mail.com",
        'password1' : "mo123456",
        'password2' : "mo123456"
    }
    client = APIClient()
    client.post('/authentication/register/', user)
    response1 = client.post('/authentication/login/', {'username' : "MuhammedKhedr"})
    assert response1.status_code == 400

################## Logout Testing ##################

@pytest.mark.django_db
def test_logout_success(auth_client):
    client = auth_client()
    response = client.post('/authentication/logout/')

    assert response.status_code == 204
    
    
@pytest.mark.django_db
def test_logout_fail():
    client = APIClient()
    response = client.post('/authentication/logout/')

    assert response.status_code == 401