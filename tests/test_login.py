"""
tests/test_login.py
====================
Test Module: Login Functionality
Application: OrangeHRM Demo (https://opensource-demo.orangehrmlive.com)

Test Cases:
    TC_LOGIN_001  Valid login with correct credentials
    TC_LOGIN_002  Invalid login - wrong password
    TC_LOGIN_003  Invalid login - wrong username
    TC_LOGIN_004  Invalid login - both fields wrong
    TC_LOGIN_005  Empty username submission
    TC_LOGIN_006  Empty password submission
    TC_LOGIN_007  Empty both fields submission
    TC_LOGIN_008  Login page UI elements are visible
    TC_LOGIN_009  Forgot Password link is visible and navigates correctly
    TC_LOGIN_010  Successful logout after login
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    EMPTY_USERNAME,
    EMPTY_PASSWORD,
)


@pytest.fixture(autouse=True)
def open_login_page(driver):
    """Navigate to the login page before each test in this module."""
    driver.get(BASE_URL)


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_001 — Valid Login
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login_redirects_to_dashboard(driver):
    """
    TC_LOGIN_001
    GIVEN  a valid username and password
    WHEN   the user submits the login form
    THEN   the user should be redirected to the dashboard
    """
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_loaded(), \
        "Dashboard header not visible after valid login"
    assert "dashboard" in driver.current_url.lower(), \
        f"Expected URL to contain 'dashboard', got: {driver.current_url}"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_002 — Wrong Password
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_invalid_login_wrong_password_shows_error(driver):
    """
    TC_LOGIN_002
    GIVEN  a valid username and an incorrect password
    WHEN   the user submits the login form
    THEN   an error message should be displayed
    AND    the user should remain on the login page
    """
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)

    error = login_page.get_error_message()
    assert "Invalid credentials" in error, \
        f"Expected 'Invalid credentials' error, got: '{error}'"
    assert "login" in driver.current_url.lower(), \
        "User should remain on login page after failed login"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_003 — Wrong Username
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_invalid_login_wrong_username_shows_error(driver):
    """
    TC_LOGIN_003
    GIVEN  an invalid username and a correct password
    WHEN   the user submits the login form
    THEN   an error message should be displayed
    """
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)

    error = login_page.get_error_message()
    assert "Invalid credentials" in error, \
        f"Expected 'Invalid credentials' error, got: '{error}'"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_004 — Both Fields Wrong
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_invalid_login_both_wrong_shows_error(driver):
    """
    TC_LOGIN_004
    GIVEN  an invalid username and an invalid password
    WHEN   the user submits the login form
    THEN   an error message should be displayed
    """
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    error = login_page.get_error_message()
    assert len(error) > 0, "An error message should be shown for invalid credentials"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_005 — Empty Username
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_empty_username_shows_required_alert(driver):
    """
    TC_LOGIN_005
    GIVEN  an empty username field and a valid password
    WHEN   the user submits the login form
    THEN   a required field alert should appear for the username
    """
    login_page = LoginPage(driver)
    login_page.login(EMPTY_USERNAME, VALID_PASSWORD)

    alerts = login_page.get_required_field_alerts()
    assert len(alerts) >= 1, "Expected at least 1 required field alert"
    assert any("Required" in a.text for a in alerts), \
        "Expected 'Required' validation message"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_006 — Empty Password
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_empty_password_shows_required_alert(driver):
    """
    TC_LOGIN_006
    GIVEN  a valid username and an empty password field
    WHEN   the user submits the login form
    THEN   a required field alert should appear for the password
    """
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, EMPTY_PASSWORD)

    alerts = login_page.get_required_field_alerts()
    assert len(alerts) >= 1, "Expected at least 1 required field alert"
    assert any("Required" in a.text for a in alerts), \
        "Expected 'Required' validation message"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_007 — Both Fields Empty
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_both_fields_empty_shows_two_required_alerts(driver):
    """
    TC_LOGIN_007
    GIVEN  both username and password fields are empty
    WHEN   the user clicks the Login button
    THEN   required field alerts should appear for both fields
    """
    login_page = LoginPage(driver)
    login_page.login(EMPTY_USERNAME, EMPTY_PASSWORD)

    alerts = login_page.get_required_field_alerts()
    assert len(alerts) == 2, \
        f"Expected 2 required field alerts, got {len(alerts)}"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_008 — UI Elements Visible
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.login
def test_login_page_ui_elements_are_visible(driver):
    """
    TC_LOGIN_008
    GIVEN  the login page is loaded
    THEN   the OrangeHRM logo and Forgot Password link should be visible
    """
    login_page = LoginPage(driver)
    assert login_page.is_logo_displayed(), "OrangeHRM logo should be visible"
    assert login_page.is_forgot_password_visible(), \
        "Forgot Password link should be visible"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_009 — Forgot Password Navigation
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.login
def test_forgot_password_link_navigates_correctly(driver):
    """
    TC_LOGIN_009
    GIVEN  the user is on the login page
    WHEN   the user clicks 'Forgot your password?'
    THEN   the URL should change to the reset password page
    """
    login_page = LoginPage(driver)
    login_page.click_forgot_password()

    assert "requestPasswordResetCode" in driver.current_url or \
           "forgot" in driver.current_url.lower(), \
           f"Expected password reset URL, got: {driver.current_url}"


# ─────────────────────────────────────────────────────────────
# TC_LOGIN_010 — Logout
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.login
def test_logout_redirects_to_login_page(driver):
    """
    TC_LOGIN_010
    GIVEN  the user is logged in
    WHEN   the user clicks Logout
    THEN   the user should be redirected back to the login page
    """
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_loaded(), "Must be on dashboard before logout"

    dashboard_page.logout()
    assert "login" in driver.current_url.lower(), \
        f"Expected login URL after logout, got: {driver.current_url}"
