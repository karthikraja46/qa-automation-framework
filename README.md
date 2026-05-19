# OrangeHRM QA Automation Framework

![CI Status](https://github.com/YOUR_USERNAME/qa-automation-framework/actions/workflows/qa-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/selenium-4.18-green)
![pytest](https://img.shields.io/badge/pytest-8.1-orange)

A production-grade test automation framework built with **Python + pytest + Selenium WebDriver** targeting the [OrangeHRM Demo Application](https://opensource-demo.orangehrmlive.com). Implements the **Page Object Model (POM)** design pattern for maintainability and scalability, with a **GitHub Actions CI/CD pipeline** that runs tests automatically on every push.

---

## Project Structure

```
qa-automation-framework/
├── pages/                      # Page Object Model classes
│   ├── base_page.py            # BasePage — shared Selenium interactions
│   ├── login_page.py           # Login page locators + actions
│   ├── dashboard_page.py       # Dashboard page locators + actions
│   └── employee_page.py        # PIM/Employee page locators + actions
│
├── tests/                      # Test modules
│   ├── test_login.py           # 10 login test cases (positive + negative)
│   ├── test_dashboard.py       # 6 dashboard test cases
│   └── test_employee.py        # 6 employee/PIM test cases
│
├── utils/
│   ├── config.py               # Central config — URLs, credentials, timeouts
│   └── helpers.py              # Explicit waits, screenshot utilities
│
├── reports/                    # Auto-generated HTML test reports
├── .github/workflows/
│   └── qa-tests.yml            # GitHub Actions CI/CD pipeline
│
├── conftest.py                 # Shared pytest fixtures (driver setup/teardown)
├── pytest.ini                  # pytest config — markers, report settings
├── requirements.txt            # Python dependencies
└── README.md
```

---

## Test Coverage

### Test Suite Summary

| Module | Total TCs | Smoke | Regression | Positive | Negative |
|---|---|---|---|---|---|
| Login | 10 | 3 | 7 | 3 | 7 |
| Dashboard | 6 | 2 | 4 | 6 | 0 |
| Employee (PIM) | 6 | 3 | 3 | 5 | 1 |
| **Total** | **22** | **8** | **14** | **14** | **8** |

### Test Case Traceability Matrix

| Test Case ID | Description | Type | Priority | Status |
|---|---|---|---|---|
| TC_LOGIN_001 | Valid login redirects to dashboard | Smoke | P0 | ✅ Active |
| TC_LOGIN_002 | Invalid login — wrong password shows error | Regression | P1 | ✅ Active |
| TC_LOGIN_003 | Invalid login — wrong username shows error | Regression | P1 | ✅ Active |
| TC_LOGIN_004 | Invalid login — both fields wrong | Regression | P1 | ✅ Active |
| TC_LOGIN_005 | Empty username — required alert shown | Regression | P2 | ✅ Active |
| TC_LOGIN_006 | Empty password — required alert shown | Regression | P2 | ✅ Active |
| TC_LOGIN_007 | Both fields empty — two required alerts | Regression | P2 | ✅ Active |
| TC_LOGIN_008 | Login page UI elements are visible | Smoke | P1 | ✅ Active |
| TC_LOGIN_009 | Forgot password navigates correctly | Regression | P2 | ✅ Active |
| TC_LOGIN_010 | Logout redirects to login page | Smoke | P0 | ✅ Active |
| TC_DASH_001 | Dashboard loads after login | Smoke | P0 | ✅ Active |
| TC_DASH_002 | Sidebar navigation is visible | Smoke | P1 | ✅ Active |
| TC_DASH_003 | Dashboard widgets are present | Regression | P2 | ✅ Active |
| TC_DASH_004 | Navigate to PIM from sidebar | Regression | P1 | ✅ Active |
| TC_DASH_005 | Navigate to Admin from sidebar | Regression | P1 | ✅ Active |
| TC_DASH_006 | Logged-in username is displayed | Regression | P2 | ✅ Active |
| TC_EMP_001 | Employee list page loads | Smoke | P0 | ✅ Active |
| TC_EMP_002 | Search existing employee returns results | Regression | P1 | ✅ Active |
| TC_EMP_003 | Search non-existent employee — no records | Regression | P2 | ✅ Active |
| TC_EMP_004 | Reset search clears filter | Regression | P2 | ✅ Active |
| TC_EMP_005 | Default employee list has records | Smoke | P1 | ✅ Active |
| TC_EMP_006 | Add Employee button is visible | Smoke | P1 | ✅ Active |

---

## Design Patterns

### Page Object Model (POM)
All locators and page interactions are encapsulated inside dedicated Page classes. Tests never call Selenium directly — they call Page methods. This means a locator change only needs to be updated in one place.

```
Test File  →  Page Object  →  BasePage  →  Selenium WebDriver
```

### Fixture Architecture
- `driver` — creates and tears down a fresh Chrome instance per test
- `logged_in_driver` — pre-authenticated session; reused in dashboard/employee tests
- `autouse=True` fixtures — handle navigation setup without repetition in every test

### Explicit Waits Over Implicit Waits
All element interactions use explicit waits (`WebDriverWait` + `expected_conditions`) for reliability. Implicit waits are only used as a safety net.

---

## Setup & Local Execution

### Prerequisites
- Python 3.9+
- Google Chrome installed
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/qa-automation-framework.git
cd qa-automation-framework

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate          # Mac/Linux
venv\Scripts\activate             # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run smoke tests only
pytest -m smoke

# Run regression suite only
pytest -m regression

# Run a specific module
pytest tests/test_login.py

# Run negative tests only
pytest -m negative

# Run with verbose output
pytest -v

# Run and open HTML report
pytest && open reports/report.html
```

---

## CI/CD Pipeline

Tests run automatically on GitHub Actions on every push to `main` or `develop`, and on every pull request.

**Pipeline steps:**
1. Checkout code
2. Set up Python 3.11
3. Cache pip dependencies
4. Install project requirements
5. Install Google Chrome
6. Run smoke tests (blocking — pipeline fails if smoke fails)
7. Run regression suite
8. Upload HTML report as downloadable artifact (retained 14 days)
9. Upload failure screenshots on test failure (retained 7 days)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Test Framework | pytest 8.1 |
| Browser Automation | Selenium 4.18 |
| Driver Management | webdriver-manager |
| Reporting | pytest-html |
| CI/CD | GitHub Actions |
| Design Pattern | Page Object Model (POM) |
| Target Application | OrangeHRM Demo |

---
