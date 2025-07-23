from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import allure
from typing import List, Optional, Any
from utils.config import Config

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class containing common methods for all page objects"""

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)

    @allure.step("Navigate to URL: {url}")
    def navigate_to(self, url: str) -> None:
        """Navigate to the specified URL"""
        try:
            self.driver.get(url)
            logger.info(f"Navigated to: {url}")
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {str(e)}")
            raise

    @allure.step("Find element by locator")
    def find_element(self, locator: tuple, timeout: int = None) -> Any:
        """Find element with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
            logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not found within {wait_time} seconds: {locator}")
            raise

    @allure.step("Find elements by locator")
    def find_elements(self, locator: tuple, timeout: int = None) -> List[Any]:
        """Find multiple elements with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            elements = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located(locator)
            )
            logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"Elements not found within {wait_time} seconds: {locator}")
            return []

    @allure.step("Click element")
    def click_element(self, locator: tuple, timeout: int = None) -> None:
        """Click element after ensuring it's clickable"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logger.info(f"Clicked element: {locator}")
        except TimeoutException:
            logger.error(f"Element not clickable within {wait_time} seconds: {locator}")
            raise

    @allure.step("Enter text: {text}")
    def enter_text(self, locator: tuple, text: str, clear_first: bool = True) -> None:
        """Enter text into input field"""
        try:
            element = self.find_element(locator)
            if clear_first:
                element.clear()
            element.send_keys(text)
            logger.info(f"Entered text '{text}' into element: {locator}")
        except Exception as e:
            logger.error(f"Failed to enter text into {locator}: {str(e)}")
            raise

    @allure.step("Get element text")
    def get_text(self, locator: tuple) -> str:
        """Get text from element"""
        try:
            element = self.find_element(locator)
            text = element.text
            logger.debug(f"Got text '{text}' from element: {locator}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from {locator}: {str(e)}")
            raise

    @allure.step("Get element attribute: {attribute}")
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Get attribute value from element"""
        try:
            element = self.find_element(locator)
            value = element.get_attribute(attribute)
            logger.debug(f"Got attribute '{attribute}' = '{value}' from element: {locator}")
            return value
        except Exception as e:
            logger.error(f"Failed to get attribute '{attribute}' from {locator}: {str(e)}")
            raise

    @allure.step("Check if element is displayed")
    def is_displayed(self, locator: tuple, timeout: int = None) -> bool:
        """Check if element is displayed"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            logger.debug(f"Element is displayed: {locator}")
            return True
        except TimeoutException:
            logger.debug(f"Element is not displayed: {locator}")
            return False

    @allure.step("Wait for element to disappear")
    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = None) -> bool:
        """Wait for element to disappear"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.debug(f"Element disappeared: {locator}")
            return True
        except TimeoutException:
            logger.debug(f"Element still visible after {wait_time} seconds: {locator}")
            return False

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll to element"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.debug(f"Scrolled to element: {locator}")
        except Exception as e:
            logger.error(f"Failed to scroll to element {locator}: {str(e)}")
            raise

    @allure.step("Take screenshot")
    def take_screenshot(self, name: str = "screenshot") -> None:
        """Take screenshot and attach to Allure report"""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
            logger.info(f"Screenshot taken: {name}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")

    @allure.step("Get page title")
    def get_page_title(self) -> str:
        """Get current page title"""
        title = self.driver.title
        logger.debug(f"Page title: {title}")
        return title

    @allure.step("Get current URL")
    def get_current_url(self) -> str:
        """Get current page URL"""
        url = self.driver.current_url
        logger.debug(f"Current URL: {url}")
        return url

    @allure.step("Wait for page to load")
    def wait_for_page_load(self, timeout: int = None) -> None:
        """Wait for page to fully load"""
        wait_time = timeout or Config.PAGE_LOAD_TIMEOUT
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            logger.debug("Page loaded completely")
        except TimeoutException:
            logger.warning(f"Page load timeout after {wait_time} seconds")