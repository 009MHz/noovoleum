import os
from typing import Dict, Any


class Config:

    # Browser Settings
    DEFAULT_BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    BROWSER_OPTIONS = {
        'chrome': [
            '--disable-dev-shm-usage',
            '--no-sandbox',
            '--disable-gpu',
            '--disable-extensions',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--disable-features=VizDisplayCompositor'
        ],
        'firefox': [
            '--disable-dev-shm-usage',
            '--no-sandbox'
        ],
        'edge': [
            '--disable-dev-shm-usage',
            '--no-sandbox',
            '--disable-gpu'
        ]
    }

    # Timeout Settings
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '15'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))
    SCRIPT_TIMEOUT = int(os.getenv('SCRIPT_TIMEOUT', '30'))

    # Application URLs
    BASE_URL = os.getenv('BASE_URL', 'https://noovoleum.com/id/')
    ENGLISH_URL = os.getenv('ENGLISH_URL', 'https://noovoleum.com/')

    # Test Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')
    TEST_DATA_PATH = os.getenv('TEST_DATA_PATH', 'test_data/')

    # Screenshot and Reporting
    SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'
    SCREENSHOT_PATH = os.getenv('SCREENSHOT_PATH', 'reports/screenshots/')
    ALLURE_RESULTS_PATH = os.getenv('ALLURE_RESULTS_PATH', 'reports/allure-results/')

    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'reports/test_execution.log')
    CONSOLE_LOGGING = os.getenv('CONSOLE_LOGGING', 'true').lower() == 'true'

    # Retry Settings
    MAX_RETRY_ATTEMPTS = int(os.getenv('MAX_RETRY_ATTEMPTS', '3'))
    RETRY_DELAY = float(os.getenv('RETRY_DELAY', '1.0'))

    # Performance Thresholds
    MAX_PAGE_LOAD_TIME = int(os.getenv('MAX_PAGE_LOAD_TIME', '10'))
    MAX_ELEMENT_LOAD_TIME = int(os.getenv('MAX_ELEMENT_LOAD_TIME', '5'))

    # Test Execution
    PARALLEL_EXECUTION = os.getenv('PARALLEL_EXECUTION', 'false').lower() == 'true'
    MAX_WORKERS = int(os.getenv('MAX_WORKERS', '4'))

    # Browser Download Directory
    DOWNLOAD_DIRECTORY = os.path.abspath(os.getenv('DOWNLOAD_DIRECTORY', 'reports/downloads/'))

    @classmethod
    def get_browser_options(cls, browser: str) -> list:
        """Get browser-specific options"""
        options = cls.BROWSER_OPTIONS.get(browser.lower(), [])

        if cls.HEADLESS:
            if browser.lower() == 'chrome':
                options.append('--headless=new')
            elif browser.lower() == 'firefox':
                options.append('--headless')
            elif browser.lower() == 'edge':
                options.append('--headless')

        return options

    @classmethod
    def get_chrome_prefs(cls) -> Dict[str, Any]:
        """Get Chrome browser preferences"""
        return {
            "download.default_directory": cls.DOWNLOAD_DIRECTORY,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "profile.managed_default_content_settings.images": 1
        }

    @classmethod
    def get_firefox_prefs(cls) -> Dict[str, Any]:
        """Get Firefox browser preferences"""
        return {
            "browser.download.folderList": 2,
            "browser.download.manager.showWhenStarting": False,
            "browser.download.dir": cls.DOWNLOAD_DIRECTORY,
            "browser.helperApps.neverAsk.saveToDisk": "application/pdf,application/octet-stream",
            "pdfjs.disabled": True,
            "dom.webnotifications.enabled": False,
            "dom.push.enabled": False
        }

    @classmethod
    def validate_config(cls) -> bool:
        """Validate configuration settings"""
        try:
            # Validate timeout values
            if cls.IMPLICIT_WAIT <= 0 or cls.EXPLICIT_WAIT <= 0:
                raise ValueError("Timeout values must be positive")

            # Validate URLs
            if not cls.BASE_URL or not cls.ENGLISH_URL:
                raise ValueError("URLs cannot be empty")

            # Validate paths
            os.makedirs(cls.DOWNLOAD_DIRECTORY, exist_ok=True)
            os.makedirs(cls.SCREENSHOT_PATH, exist_ok=True)
            os.makedirs(cls.ALLURE_RESULTS_PATH, exist_ok=True)

            return True
        except Exception as e:
            print(f"Configuration validation failed: {str(e)}")
            return False

    @classmethod
    def print_config(cls):
        """Print current configuration for debugging"""
        config_info = f"""
        ===== Noovoleum Test Configuration =====
        Browser: {cls.DEFAULT_BROWSER}
        Headless: {cls.HEADLESS}
        Environment: {cls.ENVIRONMENT}
        Base URL: {cls.BASE_URL}

        Timeouts:
        - Implicit Wait: {cls.IMPLICIT_WAIT}s
        - Explicit Wait: {cls.EXPLICIT_WAIT}s
        - Page Load: {cls.PAGE_LOAD_TIMEOUT}s

        Paths:
        - Screenshots: {cls.SCREENSHOT_PATH}
        - Downloads: {cls.DOWNLOAD_DIRECTORY}
        - Allure Results: {cls.ALLURE_RESULTS_PATH}

        Execution:
        - Parallel: {cls.PARALLEL_EXECUTION}
        - Max Workers: {cls.MAX_WORKERS}
        - Max Retries: {cls.MAX_RETRY_ATTEMPTS}
        ==========================================
        """
        print(config_info)
