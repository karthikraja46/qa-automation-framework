"""
utils/helpers.py - Reusable helper utilities for the QA framework.
Centralises common wait strategies and screenshot capture.
"""

import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.config import EXPLICIT_WAIT


def wait_for_element_visible(driver, locator, timeout=EXPLICIT_WAIT):
    """
    Explicitly wait for an element to be visible on the page.
    Returns the element, or raises TimeoutException if not found.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        raise TimeoutException(
            f"Element with locator {locator} was not visible within {timeout}s"
        )


def wait_for_element_clickable(driver, locator, timeout=EXPLICIT_WAIT):
    """
    Explicitly wait for an element to be clickable.
    Returns the element, or raises TimeoutException.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    except TimeoutException:
        raise TimeoutException(
            f"Element with locator {locator} was not clickable within {timeout}s"
        )


def wait_for_url_contains(driver, partial_url, timeout=EXPLICIT_WAIT):
    """
    Wait until the current URL contains the given substring.
    Useful for confirming navigation after login/redirect.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.url_contains(partial_url)
        )
    except TimeoutException:
        raise TimeoutException(
            f"URL did not contain '{partial_url}' within {timeout}s. "
            f"Current URL: {driver.current_url}"
        )


def take_screenshot(driver, name="screenshot"):
    """
    Saves a PNG screenshot to the reports/ directory.
    Useful for attaching failure evidence to test reports.
    """
    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    path = f"reports/screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path
