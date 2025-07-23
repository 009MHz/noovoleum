from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from utils.config import Config

logger = logging.getLogger(__name__)


class DriverFactory:
    """Factory class for creating WebDriver instances"""

    @staticmethod
    def create_driver() -> webdriver.Chrome:
        """Create and configure Chrome WebDriver instance"""
        try:
            # Chrome options
            options = Options()

            # Add configuration options
            for option in Config.get_chrome_options():
                options.add_argument(option)

            # Set window size
            options.add_argument(f'--window-size={Config.WINDOW_WIDTH},{Config.WINDOW_HEIGHT}')

            # Additional Chrome preferences
            prefs = {
                "profile.default_content_setting_values": {
                    "notifications": 2,  # Block notifications
                    "media_stream": 2,  # Block camera/microphone
                },
                "profile.managed_default_content_settings": {
                    "images": 2  # Block images for faster loading (optional)
                }
            }
            options.add_experimental_option("prefs", prefs)

            # Create service
            service = Service(ChromeDriverManager().install())

            # Create driver
            driver = webdriver.Chrome(service=service, options=options)

            # Set timeouts
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

            # Maximize window if not headless
            if not Config.HEADLESS:
                driver.maximize_window()

            logger.info("Chrome WebDriver created successfully")
            return driver

        except Exception as e:
            logger.error(f"Failed to create WebDriver: {str(e)}")
            raise

    @staticmethod
    def quit_driver(driver: webdriver.Chrome) -> None:
        """Safely quit the WebDriver"""
        if driver:
            try:
                driver.quit()
                logger.info("WebDriver quit successfully")
            except Exception as e:
                logger.error(f"Error quitting WebDriver: {str(e)}")