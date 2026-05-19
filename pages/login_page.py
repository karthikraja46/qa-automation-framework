"""
pages/login_page.py - Login Page Object
Encapsulates all locators and actions for the OrangeHRM login screen.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the OrangeHRM Login page.
    URL: /web/index.php/auth/login
    """

    # ── Locators ─────────────────────────────────────────────
    USERNAME_INPUT   = (By.NAME, "username")
    PASSWORD_INPUT   = (By.NAME, "password")
    LOGIN_BUTTON     = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE    = (By.XPATH, "//div[contains(@class,'orangehrm-login-error')]//p")
    REQUIRED_ALERT   = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")
    PAGE_LOGO        = (By.XPATH, "//div[contains(@class,'orangehrm-login-logo')]")
    FORGOT_PASSWORD  = (By.XPATH, "//p[normalize-space()='Forgot your password?']")

    # ── Actions ──────────────────────────────────────────────

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Full login sequence: enter credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Assertions helpers ────────────────────────────────────

    def get_error_message(self):
        """Return the error message text shown on invalid login."""
        return self.get_text(self.ERROR_MESSAGE)

    def get_required_field_alerts(self):
        """Return all required-field alert elements (for empty submission)."""
        from selenium.webdriver.support import expected_conditions as EC
        return self.wait.until(
            EC.presence_of_all_elements_located(self.REQUIRED_ALERT)
        )

    def is_logo_displayed(self):
        return self.is_displayed(self.PAGE_LOGO)

    def is_forgot_password_visible(self):
        return self.is_displayed(self.FORGOT_PASSWORD)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)
