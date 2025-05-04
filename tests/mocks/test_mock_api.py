import requests

def test_mock_example():
    response = requests.get("https://postman-echo.com/get?foo=bar")
    data = response.json()
    assert response.status_code == 200
    assert data['args']['foo'] == 'bar'
