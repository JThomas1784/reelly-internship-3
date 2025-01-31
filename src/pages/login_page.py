from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BUTTON = (By.LINK_TEXT, "Continue")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click(*self.LOGIN_BUTTON)
