"""
pages/dashboard_page.py - Dashboard Page Object
Encapsulates locators and actions for the OrangeHRM main dashboard.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page Object for the OrangeHRM Dashboard.
    URL: /web/index.php/dashboard/index
    """

    # ── Locators ─────────────────────────────────────────────
    DASHBOARD_HEADER     = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    USER_DROPDOWN        = (By.XPATH, "//li[contains(@class,'oxd-userdropdown')]")
    USER_PROFILE_NAME    = (By.XPATH, "//p[contains(@class,'oxd-userdropdown-name')]")
    LOGOUT_OPTION        = (By.XPATH, "//a[normalize-space()='Logout']")
    SIDE_NAV             = (By.XPATH, "//nav[contains(@class,'oxd-sidepanel-body')]")

    # ── Sidebar menu items ────────────────────────────────────
    ADMIN_MENU           = (By.XPATH, "//span[normalize-space()='Admin']")
    PIM_MENU             = (By.XPATH, "//span[normalize-space()='PIM']")
    MY_INFO_MENU         = (By.XPATH, "//span[normalize-space()='My Info']")
    LEAVE_MENU           = (By.XPATH, "//span[normalize-space()='Leave']")
    RECRUITMENT_MENU     = (By.XPATH, "//span[normalize-space()='Recruitment']")

    # ── Widget headings ───────────────────────────────────────
    WIDGET_HEADINGS      = (By.XPATH, "//p[contains(@class,'oxd-text--card-title')]")

    # ── Actions ──────────────────────────────────────────────

    def is_dashboard_loaded(self):
        """Confirm the dashboard header is visible — used post-login assertion."""
        return self.is_displayed(self.DASHBOARD_HEADER)

    def get_logged_in_username(self):
        """Return the name shown in the top-right user dropdown."""
        return self.get_text(self.USER_PROFILE_NAME)

    def logout(self):
        """Click the user dropdown and select Logout."""
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)

    def navigate_to_pim(self):
        self.click(self.PIM_MENU)

    def navigate_to_admin(self):
        self.click(self.ADMIN_MENU)

    def navigate_to_leave(self):
        self.click(self.LEAVE_MENU)

    def get_visible_widget_headings(self):
        """Return a list of visible widget heading texts on the dashboard."""
        from selenium.webdriver.support import expected_conditions as EC
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.WIDGET_HEADINGS)
        )
        return [el.text for el in elements]

    def is_side_nav_visible(self):
        return self.is_displayed(self.SIDE_NAV)
