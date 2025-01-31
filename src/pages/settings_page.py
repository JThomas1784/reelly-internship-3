from selenium.webdriver.common.by import By
from .base_page import BasePage

class SettingsPage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//*[@id='w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b']/div[1]/div[2]/div/a[16]")
    VERIFICATION_LINK = (By.XPATH, "/html/body/div[3]/div[2]/a[11]")
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "/html/body/div[3]/div/div[4]/label")
    NEXT_STEP_BUTTON = (By.XPATH, "/html/body/div[3]/div/a")
    VERIFICATION_PAGE_TITLE = "Upload your photo"


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

