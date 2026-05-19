"""
pages/employee_page.py - PIM / Employee List Page Object
Encapsulates locators and actions for employee search and management.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EmployeePage(BasePage):
    """
    Page Object for the PIM > Employee List page.
    URL: /web/index.php/pim/viewEmployeeList
    """

    # ── Locators ─────────────────────────────────────────────
    PAGE_HEADER          = (By.XPATH, "//h5[normalize-space()='Employee Information']")
    SEARCH_NAME_INPUT    = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    SEARCH_BUTTON        = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON         = (By.XPATH, "//button[@type='reset']")
    ADD_EMPLOYEE_BUTTON  = (By.XPATH, "//a[normalize-space()='Add Employee']")
    EMPLOYEE_ROWS        = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    NO_RECORDS_FOUND     = (By.XPATH, "//span[normalize-space()='No Records Found']")
    RECORD_COUNT         = (By.XPATH, "//span[contains(@class,'oxd-text--span') and contains(text(),'Record')]")

    # Add Employee form locators
    FIRST_NAME_INPUT     = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT    = (By.NAME, "middleName")
    LAST_NAME_INPUT      = (By.NAME, "lastName")
    EMPLOYEE_ID_INPUT    = (By.XPATH, "//label[normalize-space()='Employee Id']/following::input[1]")
    SAVE_BUTTON          = (By.XPATH, "//button[@type='submit']")

    # ── Actions ──────────────────────────────────────────────

    def is_employee_page_loaded(self):
        return self.is_displayed(self.PAGE_HEADER)

    def search_employee_by_name(self, name):
        """Type a name into the search box and click Search."""
        self.type_text(self.SEARCH_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)

    def reset_search(self):
        self.click(self.RESET_BUTTON)

    def get_employee_row_count(self):
        """Return the number of result rows in the employee table."""
        from selenium.webdriver.support import expected_conditions as EC
        import time
        time.sleep(1)  # allow table to re-render after search
        try:
            rows = self.driver.find_elements(*self.EMPLOYEE_ROWS)
            return len(rows)
        except Exception:
            return 0

    def is_no_records_message_visible(self):
        return self.is_displayed(self.NO_RECORDS_FOUND)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def fill_add_employee_form(self, first_name, last_name, middle_name=""):
        """Fill in the Add Employee form fields."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        if middle_name:
            self.type_text(self.MIDDLE_NAME_INPUT, middle_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def get_record_count_text(self):
        """Return the '(1) Record Found' text from the results header."""
        return self.get_text(self.RECORD_COUNT)
