from selenium import webdriver
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
import pytest

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    main_page = LoginPage(driver)
    settings_page = SettingsPage(driver)
    driver.get("https://soft.reelly.io/sign-in")

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return {"driver": driver, "main_page": main_page, "settings_page": settings_page}
