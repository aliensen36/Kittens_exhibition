import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from kittens_app.models import *
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def authenticated_client(db):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', password='testpass')
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    client._force_user = user
    return client


@pytest.fixture
def create_kitten(authenticated_client):
    breed = Breed.objects.create(name="Сиамская")
    user = authenticated_client._force_user
    return Kitten.objects.create(name="Мурзик", age=2, breed=breed, owner=user)


@pytest.mark.django_db
def test_list_breeds():
    client = APIClient()
    breed1 = Breed.objects.create(name="Сиамская")
    breed2 = Breed.objects.create(name="Мейн-Кун")
    url = reverse('breed-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['name'] == breed1.name


@pytest.mark.django_db
def test_create_kitten(authenticated_client):
    breed = Breed.objects.create(name="Сиамская")
    url = reverse('kitten-list')
    data = {
        'name': 'Котенок',
        'age': 2,
        'breed': breed.id,
        'color': 'Белый',
        'description': 'Очень игривый котенок'
    }
    response = authenticated_client.post(url, data)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Котенок'
    assert response.data['breed'] == breed.id


@pytest.mark.django_db
def test_update_kitten(authenticated_client, create_kitten):
    kitten = create_kitten
    url = reverse('kitten-detail', args=[kitten.id])
    data = {
        'name': 'Мурка',
        'color': 'Белый',
        'age': 3,
        'breed': kitten.breed.id,
        'description': 'Очень игривый котенок'
    }
    response = authenticated_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_kitten(authenticated_client, create_kitten):
    kitten = create_kitten
    url = reverse('kitten-detail', args=[kitten.id])
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_my_kittens(authenticated_client):
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(name="Мурзик", age=2, breed=breed, owner=authenticated_client._force_user)
    existing_kittens = Kitten.objects.filter(owner=authenticated_client._force_user)
    url = reverse('kitten-my-kittens')
    response = authenticated_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == existing_kittens.count()
    assert response.data[0]['name'] == kitten.name


@pytest.mark.django_db
def test_create_kitten_rating(authenticated_client):
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(name="Мурзик", age=2, breed=breed, owner=authenticated_client._force_user)
    url = reverse('kitten-rating-list')
    data = {
        'kitten': kitten.id,
        'rating': 5,
    }
    response = authenticated_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['rating'] == 5
    assert KittenRating.objects.filter(kitten=kitten, user=authenticated_client._force_user).exists()

@pytest.mark.django_db
def test_prevent_duplicate_rating(authenticated_client):
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(name="Мурзик", age=2, breed=breed, owner=authenticated_client._force_user)
    KittenRating.objects.create(kitten=kitten, user=authenticated_client._force_user, rating=5)
    url = reverse('kitten-rating-list')
    data = {
        'kitten': kitten.id,
        'rating': 4,
    }
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data
    assert response.data['error'] == 'Вы уже оценили этого котенка.'
