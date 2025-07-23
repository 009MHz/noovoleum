import pytest
import logging
import os
from datetime import datetime
from utils.browser_config import BrowserManager
from utils.config import Config
import allure

# Create reports directory and subdirectories if they don't exist
os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
os.makedirs(Config.ALLURE_RESULTS_PATH, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOG_FILE),
        logging.StreamHandler() if Config.CONSOLE_LOGGING else logging.NullHandler()
    ]
)

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browsers",
        action="store",
        default="chrome",
        help="Comma-separated list of browsers to run tests on: chrome, firefox, edge, safari"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode"
    )


def pytest_configure(config):
    """Configure pytest with custom settings"""
    # Validate configuration
    if not Config.validate_config():
        pytest.exit("Configuration validation failed")

    # Set up allure environment
    allure_env_path = os.path.join(Config.ALLURE_RESULTS_PATH, "environment.properties")
    os.makedirs(Config.ALLURE_RESULTS_PATH, exist_ok=True)

    with open(allure_env_path, "w") as f:
        f.write(f"Browsers={config.getoption('--browsers')}\n")
        f.write(f"Headless={config.getoption('--headless')}\n")
        f.write(f"Test.Execution.Date={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Register essential markers
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "critical: mark test as critical")


@pytest.fixture(scope="session", params=None)
def driver(request):
    """WebDriver fixture with browser parameterization"""
    browser = request.param.lower() if request.param else "chrome"
    headless = request.config.getoption("--headless")

    logger.info(f"Setting up {browser} driver (headless: {headless})")

    try:
        browser_manager = BrowserManager(browser, headless)
        driver_instance = browser_manager.create_webdriver()

        # Configure driver timeouts
        driver_instance.implicitly_wait(Config.IMPLICIT_WAIT)
        driver_instance.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        driver_instance.set_script_timeout(Config.SCRIPT_TIMEOUT)

        logger.info(f"Successfully created {browser} driver")
        yield driver_instance

    except Exception as e:
        logger.error(f"Failed to create {browser} driver: {str(e)}")
        pytest.fail(f"Driver setup failed for {browser}: {str(e)}")

    finally:
        if 'driver_instance' in locals():
            try:
                # Take screenshot on failure if enabled
                if hasattr(request.node, 'rep_call') and request.node.rep_call.failed and Config.SCREENSHOT_ON_FAILURE:
                    _take_failure_screenshot(driver_instance, request.node.name)

                driver_instance.quit()
                logger.info(f"Driver cleanup completed for {browser}")

            except Exception as e:
                logger.error(f"Error during driver cleanup: {str(e)}")


def pytest_generate_tests(metafunc):
    """Generate tests for each browser specified"""
    # Get the list of browsers specified in the command line options
    browsers = metafunc.config.getoption('browsers').split(',')
    browsers = [browser.strip() for browser in browsers]  # Clean up whitespace

    # Generate a separate test for each browser
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize('driver', browsers, scope='session', indirect=True)


@pytest.fixture(autouse=True)
def browser_per_test(request, driver):
    """Auto-fixture to make driver available to test classes"""
    if request.cls is not None:
        request.cls.driver = driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for failure handling"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def _take_failure_screenshot(driver, test_name):
    """Take screenshot on test failure"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"FAILED_{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)

        os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)

        driver.save_screenshot(screenshot_path)

        # Attach to Allure report
        with open(screenshot_path, "rb") as f:
            allure.attach(
                f.read(),
                name=f"Failure Screenshot - {test_name}",
                attachment_type=allure.attachment_type.PNG
            )

        logger.info(f"Failure screenshot saved: {screenshot_path}")

    except Exception as e:
        logger.error(f"Failed to take failure screenshot: {str(e)}")


# Basic test data fixture
@pytest.fixture(scope="session")
def test_data():
    """Session-scoped fixture providing common test data"""
    return {
        'valid_contact': {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message from automation'
        },
        'invalid_emails': [
            'invalid-email',
            'test@',
            '@example.com'
        ],
        'urls': {
            'base': Config.BASE_URL,
            'english': Config.ENGLISH_URL
        }
    }