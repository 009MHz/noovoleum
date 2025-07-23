import time
import allure
from pages.__base import BasePage
from elements.el_home import HomeElements
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = HomeElements()

    # Navigation Methods
    @allure.step("Navigate to Noovoleum homepage")
    def navigate_to_homepage(self):
        """Navigate to Noovoleum Indonesian homepage"""
        self.navigate_to(self.elements.URLs.BASE_URL)
        self.wait_for_page_load()
        return self

    @allure.step("Wait for preloader to disappear")
    def wait_for_preloader_to_disappear(self, timeout: int = 10) -> bool:
        """Wait for page preloader to disappear"""
        try:
            return self.wait_for_element_to_disappear(self.elements.Preloader.CONTAINER, timeout)
        except TimeoutException:
            logger.warning("Preloader did not disappear within timeout")
            return False

    # Header Section Methods
    @allure.step("Check if logo is displayed")
    def is_logo_displayed(self) -> bool:
        """Check if header logo is displayed"""
        return self.is_displayed(self.elements.Header.LOGO)

    @allure.step("Click header logo")
    def click_logo(self):
        """Click on header logo"""
        self._click(self.elements.Header.LOGO)
        return self

    @allure.step("Check if language toggle is displayed")
    def is_language_toggle_displayed(self) -> bool:
        """Check if language toggle button is displayed"""
        return self.is_displayed(self.elements.Header.LANGUAGE_TOGGLE)

    @allure.step("Get language toggle button text")
    def get_language_toggle_text(self) -> str:
        """Get language toggle button text"""
        return self.get_text(self.elements.Header.LANGUAGE_TOGGLE)

    @allure.step("Click language toggle button")
    def click_language_toggle(self):
        """Click language toggle button"""
        self._click(self.elements.Header.LANGUAGE_TOGGLE)
        time.sleep(2)  # Wait for page redirect
        return self

    @allure.step("Verify English page redirect")
    def verify_english_page_redirect(self) -> bool:
        """Verify that clicking language toggle redirects to English page"""
        current_url = self.get_current_url()
        return self.elements.URLs.ENGLISH_URL in current_url

    # Banner Section Methods
    @allure.step("Check if main heading is displayed")
    def is_main_heading_displayed(self) -> bool:
        """Check if main heading image is displayed"""
        return self.is_displayed(self.elements.Banner.MAIN_HEADING_IMAGE)

    @allure.step("Get tagline text")
    def get_tagline_text(self) -> str:
        """Get main tagline text"""
        return self.get_text(self.elements.Banner.TAGLINE)

    @allure.step("Get banner description text")
    def get_description_text(self) -> str:
        """Get banner description text"""
        return self.get_text(self.elements.Banner.DESCRIPTION_TEXT)

    @allure.step("Verify banner content")
    def verify_banner_content(self) -> tuple:
        """Verify all banner section content is present"""
        banner_checks = {
            'main_heading': self.is_main_heading_displayed(),
            'tagline': len(self.get_tagline_text()) > 0,
            'description': len(self.get_description_text()) > 0
        }
        return all(banner_checks.values()), banner_checks

    # UCOllect Process Section Methods
    @allure.step("Scroll to UCOllect section")
    def scroll_to_ucollect_section(self):
        """Scroll to UCOllect process section"""
        self.scroll_to_element(self.elements.UCOllectSection.SECTION_CONTAINER)
        return self

    @allure.step("Check if UCOllect logo is displayed")
    def is_ucollect_logo_displayed(self) -> bool:
        """Check if UCOllect logo is displayed"""
        return self.is_displayed(self.elements.UCOllectSection.UCOLLECT_LOGO)

    @allure.step("Verify process step {step_number}")
    def verify_process_step(self, step_number: int) -> tuple:
        """Verify specific process step (1-4)"""
        step_locators = {
            1: {
                'container': self.elements.UCOllectSection.STEP_1_CONTAINER,
                'image': self.elements.UCOllectSection.STEP_1_IMAGE,
                'description': self.elements.UCOllectSection.STEP_1_DESCRIPTION
            },
            2: {
                'container': self.elements.UCOllectSection.STEP_2_CONTAINER,
                'image': self.elements.UCOllectSection.STEP_2_IMAGE,
                'description': self.elements.UCOllectSection.STEP_2_DESCRIPTION
            },
            3: {
                'container': self.elements.UCOllectSection.STEP_3_CONTAINER,
                'image': self.elements.UCOllectSection.STEP_3_IMAGE,
                'description': self.elements.UCOllectSection.STEP_3_DESCRIPTION
            },
            4: {
                'container': self.elements.UCOllectSection.STEP_4_CONTAINER,
                'image': self.elements.UCOllectSection.STEP_4_IMAGE,
                'description': self.elements.UCOllectSection.STEP_4_DESCRIPTION
            }
        }

        if step_number not in step_locators:
            raise ValueError(f"Invalid step number: {step_number}. Must be 1-4")

        step = step_locators[step_number]
        step_checks = {
            'container_visible': self.is_displayed(step['container']),
            'image_visible': self.is_displayed(step['image']),
            'description_present': len(self.get_text(step['description'])) > 0
        }

        return all(step_checks.values()), step_checks

    @allure.step("Verify all UCOllect process steps")
    def verify_all_process_steps(self) -> tuple:
        """Verify all 4 UCOllect process steps"""
        all_steps_valid = True
        step_results = {}

        for step_num in range(1, 5):
            is_valid, checks = self.verify_process_step(step_num)
            step_results[f'step_{step_num}'] = checks
            if not is_valid:
                all_steps_valid = False

        return all_steps_valid, step_results

    # App Download Section Methods
    @allure.step("Scroll to app download section")
    def scroll_to_app_download_section(self):
        """Scroll to app download section"""
        self.scroll_to_element(self.elements.AppDownload.SECTION_CONTAINER)
        return self

    @allure.step("Check if app download title is displayed")
    def is_app_download_title_displayed(self) -> bool:
        """Check if app download title is displayed"""
        return self.is_displayed(self.elements.AppDownload.DOWNLOAD_TITLE)

    @allure.step("Get app download title text")
    def get_app_download_title(self) -> str:
        """Get app download title text"""
        return self.get_text(self.elements.AppDownload.DOWNLOAD_TITLE)

    @allure.step("Get app download description")
    def get_app_download_description(self) -> str:
        """Get app download description text"""
        return self.get_text(self.elements.AppDownload.DOWNLOAD_DESCRIPTION)

    @allure.step("Check if App Store button is displayed")
    def is_app_store_button_displayed(self) -> bool:
        """Check if App Store download button is displayed"""
        return self.is_displayed(self.elements.AppDownload.APP_STORE_IMAGE)

    @allure.step("Check if Google Play button is displayed")
    def is_google_play_button_displayed(self) -> bool:
        """Check if Google Play download button is displayed"""
        return self.is_displayed(self.elements.AppDownload.GOOGLE_PLAY_IMAGE)

    @allure.step("Click App Store download button")
    def click_app_store_button(self):
        """Click App Store download button"""
        self._click(self.elements.AppDownload.APP_STORE_LINK)
        return self

    @allure.step("Click Google Play download button")
    def click_google_play_button(self):
        """Click Google Play download button"""
        self._click(self.elements.AppDownload.GOOGLE_PLAY_LINK)
        return self

    @allure.step("Verify app store link URL")
    def verify_app_store_link_url(self) -> bool:
        """Verify App Store link points to correct URL"""
        href = self.get_attribute(self.elements.AppDownload.APP_STORE_LINK, 'href')
        return self.elements.URLs.APP_STORE_URL in href

    @allure.step("Verify Google Play link URL")
    def verify_google_play_link_url(self) -> bool:
        """Verify Google Play link points to correct URL"""
        href = self.get_attribute(self.elements.AppDownload.GOOGLE_PLAY_LINK, 'href')
        return self.elements.URLs.GOOGLE_PLAY_URL in href

    # Contact Form Methods
    @allure.step("Scroll to contact section")
    def scroll_to_contact_section(self):
        """Scroll to contact form section"""
        self.scroll_to_element(self.elements.Contact.SECTION_CONTAINER)
        return self

    @allure.step("Check if contact form is displayed")
    def is_contact_form_displayed(self) -> bool:
        """Check if contact form is displayed"""
        return self.is_displayed(self.elements.Contact.CONTACT_FORM)

    @allure.step("Get contact form title")
    def get_contact_title(self) -> str:
        """Get contact form title text"""
        return self.get_text(self.elements.Contact.CONTACT_TITLE)

    @allure.step("Fill contact form with name: {name}, email: {email}")
    def fill_contact_form(self, name: str, email: str, message: str):
        """Fill contact form with provided data"""
        self.enter_text(self.elements.Contact.NAME_FIELD, name)
        self.enter_text(self.elements.Contact.EMAIL_FIELD, email)
        self.enter_text(self.elements.Contact.MESSAGE_FIELD, message)
        return self

    @allure.step("Clear contact form")
    def clear_contact_form(self):
        """Clear all contact form fields"""
        self._find(self.elements.Contact.NAME_FIELD).clear()
        self._find(self.elements.Contact.EMAIL_FIELD).clear()
        self._find(self.elements.Contact.MESSAGE_FIELD).clear()
        return self

    @allure.step("Click send message button")
    def click_send_message_button(self):
        """Click send message button"""
        self._click(self.elements.Contact.SEND_BUTTON)
        return self

    @allure.step("Submit contact form with test data")
    def submit_contact_form_with_test_data(self):
        """Submit contact form with valid test data"""
        self.fill_contact_form(
            self.elements.TestData.VALID_NAME,
            self.elements.TestData.VALID_EMAIL,
            self.elements.TestData.VALID_MESSAGE
        )
        self.click_send_message_button()
        return self

    # Footer Section Methods
    @allure.step("Scroll to footer section")
    def scroll_to_footer_section(self):
        """Scroll to footer section"""
        self.scroll_to_element(self.elements.Footer.LOGO)
        return self

    @allure.step("Check if footer logo is displayed")
    def is_footer_logo_displayed(self) -> bool:
        """Check if footer logo is displayed"""
        return self.is_displayed(self.elements.Footer.LOGO)

    @allure.step("Click LinkedIn link")
    def click_linkedin_link(self):
        """Click LinkedIn social media link"""
        self._click(self.elements.Footer.LINKEDIN_LINK)
        return self

    @allure.step("Click Instagram link")
    def click_instagram_link(self):
        """Click Instagram social media link"""
        self._click(self.elements.Footer.INSTAGRAM_LINK)
        return self

    @allure.step("Click email link")
    def click_email_link(self):
        """Click email contact link"""
        self._click(self.elements.Footer.EMAIL_LINK)
        return self

    @allure.step("Verify LinkedIn link URL")
    def verify_linkedin_link_url(self) -> bool:
        """Verify LinkedIn link points to correct URL"""
        href = self.get_attribute(self.elements.Footer.LINKEDIN_LINK, 'href')
        return self.elements.URLs.LINKEDIN_URL in href

    @allure.step("Verify Instagram link URL")
    def verify_instagram_link_url(self) -> bool:
        """Verify Instagram link points to correct URL"""
        href = self.get_attribute(self.elements.Footer.INSTAGRAM_LINK, 'href')
        return self.elements.URLs.INSTAGRAM_URL in href

    @allure.step("Verify email link")
    def verify_email_link(self) -> bool:
        """Verify email link is correct"""
        href = self.get_attribute(self.elements.Footer.EMAIL_LINK, 'href')
        return self.elements.URLs.EMAIL_MAILTO in href

    @allure.step("Get copyright text")
    def get_copyright_text(self) -> str:
        """Get footer copyright text"""
        return self.get_text(self.elements.Footer.COPYRIGHT)

    # Utility Methods
    @allure.step("Verify all images are loaded")
    def verify_all_images_loaded(self) -> tuple:
        """Verify all images on the page are loaded properly"""
        images = self.find_elements(self.elements.Common.ALL_IMAGES)
        failed_images = []

        for img in images:
            try:
                # Check if image is loaded by verifying naturalWidth > 0
                is_loaded = self.driver.execute_script(
                    "return arguments[0].complete && arguments[0].naturalWidth > 0", img
                )
                if not is_loaded:
                    src = img.get_attribute('src')
                    failed_images.append(src)
            except Exception as e:
                logger.error(f"Error checking image: {str(e)}")
                failed_images.append("Unknown image")

        return len(failed_images) == 0, failed_images

    @allure.step("Scroll through entire page")
    def scroll_through_entire_page(self):
        """Scroll through the entire page to test all sections"""
        # Scroll to each major section
        self.scroll_to_ucollect_section()
        time.sleep(1)
        self.scroll_to_app_download_section()
        time.sleep(1)
        self.scroll_to_contact_section()
        time.sleep(1)
        self.scroll_to_footer_section()
        time.sleep(1)

        # Scroll back to top
        self.driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
        time.sleep(1)
        return self
