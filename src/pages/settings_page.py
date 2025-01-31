from selenium.webdriver.common.by import By
from .base_page import BasePage

class SettingsPage(BasePage):
    SETTINGS_LINK = (By.LINK_TEXT, "Settings")
    VERIFICATION_LINK = (By.LINK_TEXT, "Verification")
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "label[for='input_file']")
    NEXT_STEP_BUTTON = (By.LINK_TEXT, "Next step ->")
    VERIFICATION_PAGE_TITLE = "Step 0"


    def __init__(self, driver):
        super().__init__(driver)

    def go_to_verification_settings(self):
        self.click(*self.SETTINGS_LINK)
        self.click(*self.VERIFICATION_LINK)

    def verify_verification_page_opened(self):
      assert self.VERIFICATION_PAGE_TITLE in self.get_title(), "Verification page title is incorrect"

    def verify_elements_present(self):
        assert self.is_element_present(*self.UPLOAD_IMAGE_BUTTON), "Upload Image button is not present"
        assert self.is_element_present(*self.NEXT_STEP_BUTTON), "Next Step button is not present"

