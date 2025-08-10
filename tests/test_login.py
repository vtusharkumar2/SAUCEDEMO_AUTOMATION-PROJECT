# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("performance_glitch_user","secret_sauce")
        assert "inventory" in driver.current_url
        print("[TestLogin] ✅ Valid login passed")

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("invalid_user", "wrong_password")
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text
        print("[TestLogin] ✅ Invalid login handled correctly")