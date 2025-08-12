from utilities.utils import capture_screenshot

def test_fail_example(driver):
    driver.get("https://www.saucedemo.com/")

    # ✅ Take a screenshot without forcing a test failure
    capture_screenshot(driver, "manual_screenshot_example")

    # ✅ Use a passing assertion
    assert "Swag Labs" in driver.title