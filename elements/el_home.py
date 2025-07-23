from selenium.webdriver.common.by import By


class HomeElements:
    """Class containing all element locators for Noovoleum website"""

    # Header Section Elements
    class Header:
        NAVBAR = (By.CSS_SELECTOR, "nav.navbar.navbar-expand-md.navbar-light.bg-light.fixed-top.navbar-fixed-top")
        LOGO = (By.CSS_SELECTOR, "a.navbar-brand.back-color.scroll img")
        LANGUAGE_TOGGLE = (By.ID, "languageToggle")

    # Preloader Elements
    class Preloader:
        CONTAINER = (By.CSS_SELECTOR, ".preloader")
        LOADER = (By.CSS_SELECTOR, ".loader.loader-32")

    # Banner Section Elements
    class Banner:
        SECTION_CONTAINER = (By.CSS_SELECTOR, "section.banner-section#home")
        MAIN_HEADING_IMAGE = (By.CSS_SELECTOR, "#heading-image img")
        TAGLINE = (By.CSS_SELECTOR, "#logo-header .bp-rich-text")
        DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".header-text .bp-rich-text p")
        BANNER_LEFT_COLUMN = (By.CSS_SELECTOR, ".col-lg-6.col-md-12.col-sm-12.wow.fadeInLeft.flex.div-heading")
        BANNER_RIGHT_COLUMN = (By.CSS_SELECTOR, ".col-lg-6.col-md-12.col-sm-12.header-text.wow.fadeInRight")

    # UCOllect Process Section Elements
    class UCOllectSection:
        SECTION_CONTAINER = (By.CSS_SELECTOR, "section.services-section.greenback#services")
        UCOLLECT_LOGO = (By.CSS_SELECTOR, ".ucollect_by_noovoleum_image img")

        # Process Steps
        STEP_1_CONTAINER = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(1)")
        STEP_1_IMAGE = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(1) img")
        STEP_1_DESCRIPTION = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(1) .ucollect_step_desc .bp-rich-text p")

        STEP_2_CONTAINER = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(2)")
        STEP_2_IMAGE = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(2) img")
        STEP_2_DESCRIPTION = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(2) .ucollect_step_desc .bp-rich-text p")

        STEP_3_CONTAINER = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(3)")
        STEP_3_IMAGE = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(3) img")
        STEP_3_DESCRIPTION = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(3) .ucollect_step_desc .bp-rich-text p")

        STEP_4_CONTAINER = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(4)")
        STEP_4_IMAGE = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(4) img")
        STEP_4_DESCRIPTION = (By.CSS_SELECTOR, ".row .col-lg-3:nth-child(4) .ucollect_step_desc .bp-rich-text p")

        # All steps as a group
        ALL_STEP_CONTAINERS = (By.CSS_SELECTOR, ".service-col.left-col.top-col.wow.fadeInLeft.text-center.step_img")
        ALL_STEP_IMAGES = (By.CSS_SELECTOR, ".step_img img")
        ALL_STEP_DESCRIPTIONS = (By.CSS_SELECTOR, ".ucollect_step_desc .bp-rich-text p")

    # App Download Section Elements
    class AppDownload:
        SECTION_CONTAINER = (By.CSS_SELECTOR, "section.blog-section#about")
        APP_IMAGE_SVG = (By.CSS_SELECTOR, ".img-section svg")
        APP_IMAGE = (By.CSS_SELECTOR, ".img-section svg image")
        DOWNLOAD_TITLE = (By.CSS_SELECTOR, ".ucollect-download-title .bp-rich-text p")
        DOWNLOAD_DESCRIPTION = (By.CSS_SELECTOR, ".ucollect-download-desc .bp-rich-text p")

        # Download buttons
        APP_STORE_LINK = (By.CSS_SELECTOR, "a[href='https://noovoleum.onelink.me/1dof/xslcyjon']:first-of-type")
        APP_STORE_IMAGE = (By.CSS_SELECTOR, "a[href='https://noovoleum.onelink.me/1dof/xslcyjon']:first-of-type img")
        GOOGLE_PLAY_LINK = (By.CSS_SELECTOR, "a[href='https://noovoleum.onelink.me/1dof/xslcyjon']:last-of-type")
        GOOGLE_PLAY_IMAGE = (By.CSS_SELECTOR, "a[href='https://noovoleum.onelink.me/1dof/xslcyjon']:last-of-type img")

        # Button container
        BUTTON_CENTER = (By.CSS_SELECTOR, ".button-center")
        BUTTON_ROW = (By.CSS_SELECTOR, ".button-center .row")

    # Contact Section Elements
    class Contact:
        SECTION_CONTAINER = (By.CSS_SELECTOR, "section.contact-section#contact")
        CONTACT_TITLE = (By.CSS_SELECTOR, ".ucollect-contact-title .bp-rich-text p")

        # Contact Form
        CONTACT_FORM = (By.ID, "contact-form-data")
        FORM_ROW = (By.CSS_SELECTOR, "#contact-form-data .row")
        RESULT_CONTAINER = (By.ID, "result")

        # Form Fields
        NAME_FIELD = (By.CSS_SELECTOR, "input[name='userName']")
        EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='userEmail']")
        MESSAGE_FIELD = (By.CSS_SELECTOR, "textarea[name='userMessage']")

        # Error Message Containers
        NAME_ERROR = (By.ID, "userNameError")
        EMAIL_ERROR = (By.ID, "userEmailError")
        MESSAGE_ERROR = (By.ID, "userMessageError")

        # Submit Button
        SEND_BUTTON = (By.ID, "send-message-btn")

        # Form Validation
        REQUIRED_FIELDS = (By.CSS_SELECTOR, "input[required], textarea[required]")

    # Footer Section Elements
    class Footer:
        LOGO = (By.CSS_SELECTOR, "#logo_footer img")

        # Company Information
        SINGAPORE_COMPANY_NAME = (
        By.XPATH, "//div[contains(@class, 'media')][1]//p[contains(text(), 'NOOVOLEUM PTE. LTD.')]")
        SINGAPORE_ADDRESS_1 = (By.XPATH, "//div[contains(@class, 'media')][1]//p[contains(text(), '3 Fraser Street')]")
        SINGAPORE_ADDRESS_2 = (By.XPATH, "//div[contains(@class, 'media')][2]//p[contains(text(), 'Duo Tower')]")

        INDONESIA_COMPANY_NAME = (By.XPATH, "//p[contains(text(), 'PT PMA Noovoleum Indonesia Investama')]")
        INDONESIA_ADDRESS_1 = (By.XPATH, "//p[contains(text(), 'Jl. Raden Patah')]")
        INDONESIA_ADDRESS_2 = (By.XPATH, "//p[contains(text(), 'Coblong, Kota Bandung')]")

        # Social Media Links
        LINKEDIN_LINK = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/noovoleum/']")
        LINKEDIN_ICON = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/noovoleum/'] .fab.fa-linkedin-in")
        LINKEDIN_TEXT = (
        By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/noovoleum/'] .media-body .bp-rich-text p")

        INSTAGRAM_LINK = (By.CSS_SELECTOR, "a[href='https://www.instagram.com/noovoleumid/']")
        INSTAGRAM_ICON = (By.CSS_SELECTOR, "a[href='https://www.instagram.com/noovoleumid/'] .fab.fa-instagram")
        INSTAGRAM_TEXT = (
        By.CSS_SELECTOR, "a[href='https://www.instagram.com/noovoleumid/'] .media-body .bp-rich-text p")

        EMAIL_LINK = (By.CSS_SELECTOR, "a[href='mailto:contact@noovoleum.com']")
        EMAIL_ICON = (By.CSS_SELECTOR, "a[href='mailto:contact@noovoleum.com'] .far.fa-paper-plane")
        EMAIL_TEXT = (By.CSS_SELECTOR, "a[href='mailto:contact@noovoleum.com'] .media-body .bp-rich-text p")

        # Footer Links
        COPYRIGHT = (By.CSS_SELECTOR, ".copyright .bp-rich-text")
        SELF_DECLARATION_LINK = (By.CSS_SELECTOR, "a[href='/id/self-declaration']")
        PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "a[href='/privacy-policy']")
        TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "a[href='/id/syarat-dan-ketentuan-2024']")

        # All footer links
        ALL_FOOTER_LINKS = (By.CSS_SELECTOR, ".copyright a")

    # Animation Elements
    class Animations:
        WOW_ELEMENTS = (By.CSS_SELECTOR, ".wow")
        FADE_IN_LEFT = (By.CSS_SELECTOR, ".wow.fadeInLeft")
        FADE_IN_RIGHT = (By.CSS_SELECTOR, ".wow.fadeInRight")
        FADE_IN_DOWN = (By.CSS_SELECTOR, ".wow.fadeInDown")

    # Common Elements
    class Common:
        BODY = (By.TAG_NAME, "body")
        CONTAINER = (By.CSS_SELECTOR, ".container")
        CONTAINER_FLUID = (By.CSS_SELECTOR, ".container-fluid")
        ROW = (By.CSS_SELECTOR, ".row")
        COLUMNS = (By.CSS_SELECTOR, "[class*='col-']")

        # Buttons
        BUTTON = (By.CSS_SELECTOR, ".btn")
        YELLOW_BUTTON = (By.CSS_SELECTOR, ".btn.yellow-btn")
        ROUNDED_BUTTON = (By.CSS_SELECTOR, ".btn-rounded")

        # Images
        ALL_IMAGES = (By.TAG_NAME, "img")
        BP_IMAGES = (By.CSS_SELECTOR, ".bp-image-widget")

    # Validation Selectors
    class Validation:
        REQUIRED_FIELDS = (By.CSS_SELECTOR, "input[required], textarea[required]")
        EMAIL_FIELDS = (By.CSS_SELECTOR, "input[type='email']")
        TEXT_FIELDS = (By.CSS_SELECTOR, "input[type='text']")
        TEXTAREA_FIELDS = (By.TAG_NAME, "textarea")
        ALL_FORM_FIELDS = (By.CSS_SELECTOR, "input, textarea, select")
        ERROR_MESSAGES = (By.CSS_SELECTOR, ".error-message")

    # URLs and Links
    class URLs:
        BASE_URL = "https://noovoleum.com/id/"
        ENGLISH_URL = "https://noovoleum.com/"
        APP_STORE_URL = "https://noovoleum.onelink.me/1dof/xslcyjon"
        GOOGLE_PLAY_URL = "https://noovoleum.onelink.me/1dof/xslcyjon"
        LINKEDIN_URL = "https://www.linkedin.com/company/noovoleum/"
        INSTAGRAM_URL = "https://www.instagram.com/noovoleumid/"
        EMAIL_MAILTO = "mailto:contact@noovoleum.com"

    # Test Data
    class TestData:
        # Form Test Data
        VALID_NAME = "Test User"
        VALID_EMAIL = "test@example.com"
        VALID_MESSAGE = "This is a test message for automation testing."

        INVALID_EMAIL_1 = "invalid-email"
        INVALID_EMAIL_2 = "test@"
        INVALID_EMAIL_3 = "@example.com"

        LONG_NAME = "A" * 100
        LONG_MESSAGE = "This is a very long message for testing purposes. " * 10

        SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        # Expected Text Content
        EXPECTED_TAGLINE = "Making everybody a green energy champion"
        LANGUAGE_TOGGLE_TEXT = "English"

        # Contact Form Placeholders
        NAME_PLACEHOLDER = "Your Name"
        EMAIL_PLACEHOLDER = "Email Address"
        MESSAGE_PLACEHOLDER = "Write Your Message Here"

        # Company Information
        SINGAPORE_COMPANY = "NOOVOLEUM PTE. LTD."
        INDONESIA_COMPANY = "PT PMA Noovoleum Indonesia Investama"

        # Social Media Handles
        LINKEDIN_HANDLE = "noovoleum"
        INSTAGRAM_HANDLE = "noovoleumid"
        EMAIL_CONTACT = "contact@noovoleum.com"