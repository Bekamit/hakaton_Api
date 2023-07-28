import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

# @pytest.mark.django_db
# def test_api(client):
#     response = client.get('/categories/')
#     assert response.status_code == 200
#
#     response = client.get('/books/')
#     assert response.status_code == 200
#
#     data = response.json()
#     assert len(data) > 0
#
#
# @pytest.mark.djnago_db
# def test_create_book(client):
#     response = client.post('/books/', data={'title': 'Война и мир', 'price': 500}, format='json')
#
#     assert response.status_code == 401

@pytest.mark.django_db
def test_api(client):
    response = client.get('/books/')
    response = client.get('/categories/')
    response = client.get('/categories/')
    response = client.get('/categories/')



    assert response.status_code == 429