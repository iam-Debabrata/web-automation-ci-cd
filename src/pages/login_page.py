# src/pages/login_page.py
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login")
    ERROR_MSG = (By.CSS_SELECTOR, ".text-danger")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)