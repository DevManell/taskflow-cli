import requests

def test_api_connection():
    response = requests.get("https://zenquotes.io/api/random")

    assert response.status_code == 200

    data = response.json()

    assert "q" in data[0]
    assert "a" in data[0]