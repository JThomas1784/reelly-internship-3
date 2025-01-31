import pytest
from selenium import webdriver
import sys
sys.path.append(r"/Users/jamontethomas/PycharmProjects/reelly-internship-3/src")

from src.application import setup

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_verification_settings(setup):
    main_page = setup["main_page"]
    settings_page = setup["settings_page"]

    main_page.login("jamonte.thomas17@gmail.com", "9#p9PW6bLVCF8gt")
    settings_page.go_to_verification_settings()
    settings_page.verify_verification_page_opened()
    settings_page.verify_elements_present()
    print("Verification settings test passed!")