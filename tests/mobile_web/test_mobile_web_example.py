import allure
from pages.home_page import HomePage


@allure.feature("Mobile Web")
def test_homepage_heading_mobile(mobile_page, base_url):
    home = HomePage(mobile_page)
    home.navigate_to(base_url)
    assert home.get_heading() == "Example Domain"
