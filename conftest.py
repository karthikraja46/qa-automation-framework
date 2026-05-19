"""
conftest.py - Shared fixtures for OrangeHRM QA Automation Framework
All browser setup, teardown, and reusable test fixtures live here.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


# ─────────────────────────────────────────────
# Browser Fixture
# ─────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver():
    """
    Initialise a headless Chrome WebDriver for each test function.
    Yields the driver, then quits after the test completes.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()


# ─────────────────────────────────────────────
# Authenticated Session Fixture
# ─────────────────────────────────────────────

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Provides a driver that is already authenticated.
    Reuse this in any test that requires a logged-in state.
    """
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    yield driver
