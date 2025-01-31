from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//*[@id='email-2']")
    PASSWORD_INPUT = (By.XPATH, "#field")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='wf-form-Sign-up']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.click(*self.LOGIN_BUTTON)
