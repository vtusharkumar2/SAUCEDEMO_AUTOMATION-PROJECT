import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utilities.utils import capture_screenshot

@pytest.fixture()
def driver():
    print("\n[Setup] Launching browser...")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    # ✅ Disable password manager popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # ✅ Remove "Chrome is being controlled by automated software" banner
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # ✅ Reduce detection by sites
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # ✅ Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    print("\n[Teardown] Quitting browser...")
    driver.quit()

# ✅ Automatically take screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            capture_screenshot(driver, item.name)