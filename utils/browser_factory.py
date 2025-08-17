from playwright.sync_api import Playwright
from utils.config import Config


class BrowserFactory:
    """Factory for creating Playwright browsers."""

    @staticmethod
    def create_browser(playwright: Playwright):
        browser_type = getattr(playwright, Config.BROWSER)
        return browser_type.launch(headless=Config.HEADLESS)
