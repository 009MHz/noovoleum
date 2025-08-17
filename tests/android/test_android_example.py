import allure
from pages.home_page import HomePage


@allure.feature("Android")
def test_homepage_android(android_page, base_url):
    home = HomePage(android_page)
    home.navigate_to(base_url)
    assert home.get_heading() == "Example Domain"
