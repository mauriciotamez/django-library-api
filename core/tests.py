import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        email="usertest@example.com",
        password="123test",
        first_name="Bot",
        last_name="Test"
    )

    response = client.post("/api/users/", payload)

    data = response.data

    assert data["email"] == payload["email"]
    assert "password" not in data
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        email="usertest@example.com",
        password="123test",
        first_name="Bot",
        last_name="Test"
    )

    client.post("/api/users/", payload)

    response = client.post(
        "/api/token/", dict(email="usertest@example.com", password="123test"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post(
        "/api/token/", dict(email="usertest@example.com", password="123test123"))

    assert response.status_code == 401
