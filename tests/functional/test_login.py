# tests/functional/test_login.py
import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.utils.config import Config

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(browser):
    browser.get(f"{Config.BASE_URL}/login")
    login_page = LoginPage(browser)
    login_page.login("testuser", "Password@123")
    assert "profile" in browser.current_url

def test_invalid_login(browser):
    browser.get(f"{Config.BASE_URL}/login")
    login_page = LoginPage(browser)
    login_page.login("invalid", "invalid")
    assert "Invalid username or password" in login_page.get_text(login_page.ERROR_MSG)