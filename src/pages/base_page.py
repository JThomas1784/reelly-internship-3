from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def get_title(self):
        return self.driver.title

    def find_element(self, by, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))  # Use the 'by' strategy here!
            )
            return element
        except Exception as e:
            print(f"Error finding element: {e}")
            raise

    def click(self, by, locator):
        element = self.find_element(by, locator)
        element.click()

    def send_keys(self, by, locator, text):
        element = self.find_element(by, locator)
        element.send_keys(text)

    def is_element_present(self, by, locator):
        try:
            self.find_element(by, locator)
            return True
        except:
            return False