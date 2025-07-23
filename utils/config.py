import os
from typing import Dict, Any


class Config:
    """Configuration class for test settings"""

    # Base URL
    BASE_URL = os.getenv('BASE_URL', 'https://noovoleum.com/id/')

    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

    # Timeouts
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '10'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

    # Window settings
    WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', '1920'))
    WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', '1080'))

    # Chrome options
    CHROME_OPTIONS = [
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-gpu',
        '--disable-extensions',
        '--disable-infobars',
        '--disable-web-security',
        '--allow-running-insecure-content',
        '--ignore-certificate-errors',
        '--ignore-ssl-errors',
        '--ignore-certificate-errors-spki-list'
    ]

    @classmethod
    def get_chrome_options(cls) -> list:
        """Get Chrome options based on environment"""
        options = cls.CHROME_OPTIONS.copy()

        if cls.HEADLESS:
            options.extend(['--headless', '--disable-logging'])

        return options

    @classmethod
    def is_ci_environment(cls) -> bool:
        """Check if running in CI environment"""
        return os.getenv('CI', 'false').lower() == 'true'