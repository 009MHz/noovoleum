import allure
from pages.home_page import HomePage


@allure.feature("iOS")
def test_homepage_ios(ios_page, base_url):
    home = HomePage(ios_page)
    home.navigate_to(base_url)
    assert home.get_heading() == "Example Domain"
