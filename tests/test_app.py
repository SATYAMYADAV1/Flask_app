import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Pyth_prac import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data


def test_app_name():
    assert app.name == "Pyth_prac"


def test_greet_route():
    client = app.test_client()
    response = client.get("/greet/Satya")

    assert response.status_code == 200
    assert b"Hello, Satya!" in response.data
