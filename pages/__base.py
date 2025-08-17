import logging
from playwright.sync_api import Page
import allure

logger = logging.getLogger(__name__)


class BasePage:
    """Common Playwright page wrapper with Allure reporting."""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to {url}")
    def navigate_to(self, url: str) -> None:
        logger.info("Navigating to %s", url)
        self.page.goto(url)

    @allure.step("Click {selector}")
    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    @allure.step("Fill {selector}")
    def fill(self, selector: str, text: str) -> None:
        self.page.locator(selector).fill(text)

    def text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
