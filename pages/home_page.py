from .__base import BasePage
import allure
from utils.config import Config


class HomePage(BasePage):
    """Example page object for the landing page."""

    heading = "h1"

    @allure.step("Open home page")
    def open(self) -> None:
        self.navigate_to(Config.BASE_URL)

    def get_heading(self) -> str:
        return self.text(self.heading)
