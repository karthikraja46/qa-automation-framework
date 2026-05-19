"""
tests/test_dashboard.py
========================
Test Module: Dashboard Functionality
Application: OrangeHRM Demo

Test Cases:
    TC_DASH_001  Dashboard loads successfully after login
    TC_DASH_002  Sidebar navigation is visible
    TC_DASH_003  Dashboard widgets are present
    TC_DASH_004  Navigate to PIM module from sidebar
    TC_DASH_005  Navigate to Admin module from sidebar
    TC_DASH_006  Logged-in username is displayed in header
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


@pytest.fixture(autouse=True)
def login_before_each(driver):
    """Log in before every dashboard test."""
    driver.get(BASE_URL)
    LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)


# ─────────────────────────────────────────────────────────────
# TC_DASH_001 — Dashboard Loads
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.dashboard
def test_dashboard_loads_after_login(driver):
    """
    TC_DASH_001
    GIVEN  the user has logged in with valid credentials
    THEN   the dashboard page should load with its header visible
    """
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded(), \
        "Dashboard header 'Dashboard' should be visible after login"


# ─────────────────────────────────────────────────────────────
# TC_DASH_002 — Sidebar Navigation
# ─────────────────────────────────────────────────────────────
@pytest.mark.smoke
@pytest.mark.dashboard
def test_sidebar_navigation_is_visible(driver):
    """
    TC_DASH_002
    GIVEN  the user is on the dashboard
    THEN   the left sidebar navigation should be visible
    """
    dashboard = DashboardPage(driver)
    assert dashboard.is_side_nav_visible(), \
        "Sidebar navigation panel should be visible on the dashboard"


# ─────────────────────────────────────────────────────────────
# TC_DASH_003 — Dashboard Widgets Present
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_widgets_are_present(driver):
    """
    TC_DASH_003
    GIVEN  the user is on the dashboard
    THEN   at least one widget heading should be visible
    """
    dashboard = DashboardPage(driver)
    widgets = dashboard.get_visible_widget_headings()
    assert len(widgets) > 0, \
        f"Expected at least 1 dashboard widget, found {len(widgets)}"


# ─────────────────────────────────────────────────────────────
# TC_DASH_004 — Navigate to PIM
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.dashboard
def test_navigate_to_pim_module(driver):
    """
    TC_DASH_004
    GIVEN  the user is on the dashboard
    WHEN   the user clicks 'PIM' in the sidebar
    THEN   the URL should change to the PIM module
    """
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_pim()

    assert "pim" in driver.current_url.lower(), \
        f"Expected PIM URL, got: {driver.current_url}"


# ─────────────────────────────────────────────────────────────
# TC_DASH_005 — Navigate to Admin
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.dashboard
def test_navigate_to_admin_module(driver):
    """
    TC_DASH_005
    GIVEN  the user is on the dashboard
    WHEN   the user clicks 'Admin' in the sidebar
    THEN   the URL should change to the Admin module
    """
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_admin()

    assert "admin" in driver.current_url.lower(), \
        f"Expected Admin URL, got: {driver.current_url}"


# ─────────────────────────────────────────────────────────────
# TC_DASH_006 — Logged-in Username
# ─────────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.dashboard
def test_logged_in_username_is_displayed(driver):
    """
    TC_DASH_006
    GIVEN  the user is logged in as 'Admin'
    THEN   the user's display name should appear in the top-right dropdown
    """
    dashboard = DashboardPage(driver)
    username = dashboard.get_logged_in_username()
    assert len(username) > 0, \
        "Logged-in user's name should be visible in the header"
