import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from utils.browser_factory import BrowserFactory


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = BrowserFactory.create_browser(playwright_instance)
    yield browser
    browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        viewport={"width": Config.VIEWPORT_WIDTH, "height": Config.VIEWPORT_HEIGHT}
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def mobile_page(playwright_instance):
    browser = BrowserFactory.create_browser(playwright_instance)
    context = browser.new_context(**playwright_instance.devices[Config.MOBILE_DEVICE])
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def android_page(playwright_instance):
    browser = BrowserFactory.create_browser(playwright_instance)
    context = browser.new_context(**playwright_instance.devices["Pixel 5"])
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def ios_page(playwright_instance):
    browser = BrowserFactory.create_browser(playwright_instance)
    context = browser.new_context(**playwright_instance.devices["iPhone 12"])
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL
