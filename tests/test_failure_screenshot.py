import pytest

def test_fail_example(driver):
    driver.get("https://www.saucedemo.com/")
    assert "This text does not exist" in driver.page_source  # This will fail