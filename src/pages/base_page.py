from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click(self, by, locator):
        self.find_element(by, locator).click()

    def is_element_present(self, by, locator):
        try:
            self.find_element(by, locator)
            return True
        except:
            return False

    def get_title(self):
        return self.driver.title