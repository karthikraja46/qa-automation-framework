"""
tests/test_employee.py
=======================
Test Module: Employee (PIM) Management
Application: OrangeHRM Demo

Test Cases:
    TC_EMP_001  Employee list page loads after navigating to PIM
    TC_EMP_002  Search for an existing employee by name
    TC_EMP_003  Search for a non-existent employee shows no records
    TC_EMP_004  Reset search clears filters
    TC_EMP_005  Employee table displays at least one record by default
    TC_EMP_006  Add Employee button is visible
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


@pytest.fixture(autouse=True)
def login_and_navigate_to_pim(driver):
    """Log in and navigate to PIM > Employee List before each test."""
    driver.get(BASE_URL)
    LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
    DashboardPage(driver).navigate_to_pim()


# ─────────────────────────────────────────────────────────────
# TC_EMP_001 — Employee List Page Loads
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.employee
def test_employee_list_page_loads(driver):
    """
    TC_EMP_001
    GIVEN  the user navigates to PIM
    THEN   the Employee Information page header should be visible
    """
    employee_page = EmployeePage(driver)
    assert employee_page.is_employee_page_loaded(), \
        "Employee Information header should be visible on PIM page"


# ─────────────────────────────────────────────────────────────
# TC_EMP_002 — Search Existing Employee
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.employee
def test_search_existing_employee_returns_results(driver):
    """
    TC_EMP_002
    GIVEN  the user is on the Employee List page
    WHEN   the user searches for 'Admin'
    THEN   at least one result row should appear
    """
    employee_page = EmployeePage(driver)
    employee_page.search_employee_by_name("Admin")

    row_count = employee_page.get_employee_row_count()
    assert row_count >= 1, \
        f"Expected at least 1 employee result for 'Admin', got {row_count}"


# ─────────────────────────────────────────────────────────────
# TC_EMP_003 — Search Non-Existent Employee
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.employee
@pytest.mark.negative
def test_search_nonexistent_employee_shows_no_records(driver):
    """
    TC_EMP_003
    GIVEN  the user searches for a name that does not exist
    THEN   a 'No Records Found' message should be displayed
    """
    employee_page = EmployeePage(driver)
    employee_page.search_employee_by_name("ZZZZNONEXISTENTUSER99999")

    assert employee_page.is_no_records_message_visible(), \
        "Expected 'No Records Found' for a non-existent employee name"


# ─────────────────────────────────────────────────────────────
# TC_EMP_004 — Reset Search
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.employee
def test_reset_search_clears_results_filter(driver):
    """
    TC_EMP_004
    GIVEN  the user has searched for an employee
    WHEN   the user clicks Reset
    THEN   the search results should reset and show default records
    """
    employee_page = EmployeePage(driver)
    employee_page.search_employee_by_name("Admin")
    employee_page.reset_search()

    # After reset, the full default list should be visible
    row_count = employee_page.get_employee_row_count()
    assert row_count >= 1, \
        "After reset, employee table should show default records"


# ─────────────────────────────────────────────────────────────
# TC_EMP_005 — Default Table Has Records
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.employee
def test_default_employee_list_has_records(driver):
    """
    TC_EMP_005
    GIVEN  the user navigates to the Employee List page without any filter
    THEN   the table should display at least one employee record
    """
    employee_page = EmployeePage(driver)
    row_count = employee_page.get_employee_row_count()
    assert row_count >= 1, \
        f"Expected employees in default list, got {row_count} rows"


# ─────────────────────────────────────────────────────────────
# TC_EMP_006 — Add Employee Button Visible
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.employee
def test_add_employee_button_is_visible(driver):
    """
    TC_EMP_006
    GIVEN  the user is on the Employee List page
    THEN   the 'Add Employee' button should be visible and accessible
    """
    employee_page = EmployeePage(driver)
    assert employee_page.is_displayed(employee_page.ADD_EMPLOYEE_BUTTON), \
        "Add Employee button should be visible on the Employee List page"
