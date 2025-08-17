import allure
import httpx


@allure.feature("API")
def test_api_status():
    with httpx.Client() as client:
        response = client.get("https://httpbin.org/get")
    assert response.status_code == 200
