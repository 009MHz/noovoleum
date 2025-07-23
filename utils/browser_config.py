from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
import logging

logger = logging.getLogger(__name__)


class BrowserManager:
    """Browser manager to create and configure WebDriver instances"""

    def __init__(self, browser_name, headless=False):
        self.browser_name = browser_name.lower()
        self.headless = headless

    def get_browser_options(self):
        """Configure and return the appropriate WebDriver options based on the browser name and mode."""
        if self.browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif self.browser_name == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        # Common options for all browsers
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")

        # Headless mode configuration
        if self.headless:
            if self.browser_name == "firefox":
                options.add_argument("--headless")
            else:
                options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        # Chrome-specific options
        if self.browser_name == "chrome":
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('useAutomationExtension', False)

        return options

    def create_webdriver(self):
        """Create and return a WebDriver instance based on the browser name."""
        options = self.get_browser_options()

        try:
            if self.browser_name == "chrome":
                driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )

            elif self.browser_name == "firefox":
                driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=options
                )

            elif self.browser_name == "edge":
                driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=options
                )

            elif self.browser_name == "safari":
                if self.headless:
                    raise ValueError("Safari does not support headless mode")
                driver = SafariDriver()

            else:
                raise ValueError(f"Unsupported browser: {self.browser_name}")

            # Maximize the window for Firefox if not in headless mode
            if self.browser_name == "firefox" and not self.headless:
                driver.maximize_window()

            logger.info(f"Successfully created {self.browser_name} WebDriver")
            return driver

        except Exception as e:
            logger.error(f"Failed to create {self.browser_name} WebDriver: {str(e)}")

            # Fallback: try without webdriver-manager
            try:
                logger.info(f"Attempting fallback for {self.browser_name}...")
                if self.browser_name == "chrome":
                    driver = webdriver.Chrome(options=options)
                elif self.browser_name == "firefox":
                    driver = webdriver.Firefox(options=options)
                elif self.browser_name == "edge":
                    driver = webdriver.Edge(options=options)
                else:
                    raise e

                logger.info(f"Fallback successful for {self.browser_name}")
                return driver

            except Exception as fallback_error:
                logger.error(f"Fallback also failed for {self.browser_name}: {str(fallback_error)}")
                raise RuntimeError(
                    f"Failed to initialize {self.browser_name} WebDriver. "
                    f"Original error: {str(e)}. "
                    f"Fallback error: {str(fallback_error)}. "
                    f"Please ensure {self.browser_name} browser is installed."
                )