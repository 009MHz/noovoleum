import os


class Config:
    """Basic configuration for tests."""

    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1280"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "720"))
    MOBILE_DEVICE = os.getenv("MOBILE_DEVICE", "iPhone 12")
