import pytest

from Pyth_prac import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, Flask! This is my first app."


def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "This is the About page."


def test_greet_route(client):
    response = client.get("/greet/Alice")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == (
        "Hello, Alice! Welcome to Flask. jUst trying to see if it works."
    )
