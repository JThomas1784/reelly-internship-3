import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage

@pytest.fixture(scope="function")
def setup(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    main_page = LoginPage(driver)
    settings_page = SettingsPage(driver)
    driver.get("https://soft.reelly.io/sign-in")

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return {"driver": driver, "main_page": main_page, "settings_page": settings_page}