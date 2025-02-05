# src/utils/config.py
import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "10"))