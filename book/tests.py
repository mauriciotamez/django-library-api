import pytest

# This test has to be done by a staff member so the fixture (api_client) returns a client authenticated with staff access


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
    assert response.status_code == 201
    assert data["title"] == payload["title"]
