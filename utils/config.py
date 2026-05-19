"""
utils/config.py - Central configuration for the QA Automation Framework.
All environment-specific values are defined here.
For sensitive values in production, load from a .env file instead.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── Application URL ──────────────────────────────────────────
BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# ── Valid Credentials (OrangeHRM demo default) ───────────────
VALID_USERNAME = os.getenv("APP_USERNAME", "Admin")
VALID_PASSWORD = os.getenv("APP_PASSWORD", "admin123")

# ── Invalid Credentials (for negative tests) ─────────────────
INVALID_USERNAME = "invalid_user_xyz"
INVALID_PASSWORD = "wrongpassword999"
EMPTY_USERNAME   = ""
EMPTY_PASSWORD   = ""

# ── Timeouts ─────────────────────────────────────────────────
IMPLICIT_WAIT    = 10   # seconds
EXPLICIT_WAIT    = 15   # seconds
PAGE_LOAD_TIMEOUT = 30  # seconds
