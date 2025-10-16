import pytest 
from pages.login_page import LoginPage
from pages.menu_page import MenuPage

class TestLogout:
    def test_logout(self,driver):
       
        login_page=LoginPage(driver)
        menu_page=MenuPage(driver)

        login_page.load()
        login_page.login("performance_glitch_user","secret_sauce")
        menu_page.logout()

        current_url=driver.current_url

        assert "saucedemo.com" in driver.current_url, "User not redirected to login page after logout"
