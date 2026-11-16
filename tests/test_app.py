from Pyth_prac import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data


def test_app_name():
    assert app.name == "Pyth_prac"
