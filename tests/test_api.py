import requests
import pytest


def test_api_connection():
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=10
        )

        assert response.status_code == 200

        data = response.json()

        assert isinstance(data, list)
        assert "q" in data[0]

    except requests.exceptions.RequestException:
        pytest.skip("API indisponível no momento")