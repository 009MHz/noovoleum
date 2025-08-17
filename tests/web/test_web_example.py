import allure
from pages.home_page import HomePage


@allure.feature("Web")
def test_homepage_heading(page, base_url):
    home = HomePage(page)
    home.navigate_to(base_url)
    assert home.get_heading() == "Example Domain"
