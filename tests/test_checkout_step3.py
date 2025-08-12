import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utilities.utils import capture_screenshot

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# ✅ Full end-to-end checkout in a single test
def test_checkout_complete(driver):
    wait = WebDriverWait(driver, 10)

    # Step 1: Open site & login
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Step 2: Add product to cart
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Step 3: Checkout - Step 1
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Step 4: Checkout - Step 2
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Step 5: Verify Checkout Complete
    complete_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert complete_header == "Thank you for your order!"

# ✅ Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            capture_screenshot(driver, item.name)