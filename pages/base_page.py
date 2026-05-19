"""
pages/base_page.py - Base Page Object
All page classes inherit from BasePage for shared browser interactions.
This enforces DRY principles and keeps locator logic centralised.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.config import EXPLICIT_WAIT


class BasePage:
    """
    Base class for all Page Objects.
    Wraps common Selenium interactions to reduce duplication.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    # ── Core interactions ────────────────────────────────────

    def find(self, locator):
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for element to be clickable, then click."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Clear the field, then type the given text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return the visible text of an element."""
        return self.find(locator).text

    def is_displayed(self, locator):
        """Return True if element is visible on the page, False otherwise."""
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    def get_current_url(self):
        """Return the browser's current URL."""
        return self.driver.current_url

    def wait_for_url_to_contain(self, partial_url):
        """Block until the URL contains the expected substring."""
        return self.wait.until(EC.url_contains(partial_url))

    def get_title(self):
        """Return the page title."""
        return self.driver.title
