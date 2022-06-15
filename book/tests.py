import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User


@pytest.fixture
def api_client():
    user = User.objects.create_superuser(
        first_name='test', last_name='test', email='usertest@example.com', password='123test')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client

# This test has to be done by a staff member so the fixture above returns a client authenticated with staff access


@pytest.mark.django_db
def test_make_new_book(api_client):
    payload = dict(
        title="An awesome book",
        author="Mauricio Tamez",
        genre="Sci-Fi",
        description="A truly awesome book",
        date_of_publication="2022-06-15"
    )

    response = api_client.post("/api/books/", payload)

    data = response.data
    assert data["title"] == payload["title"]
