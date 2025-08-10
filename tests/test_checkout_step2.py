import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.menu_page import MenuPage  # ✅ Imported for logout

@pytest.mark.order(2)
@pytest.mark.testcase_id("TC_05_Checkout_Flow_EndToEnd")
def test_checkout_step_two(driver):
    """
    TC_05_Checkout_Flow_EndToEnd:
    This test covers the full checkout flow from login to logout including:
    - Login
    - Add item to cart
    - Checkout (Step One & Two)
    - Order confirmation
    - Logout
    """

    # ✅ Initialize Page Objects
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    menu_page = MenuPage(driver)  # ✅ For logout

    # ✅ Step 1: Login to the application
    login_page.load()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # ✅ Step 2: Add an item to the cart
    inventory_page.add_to_cart_by_product_id("sauce-labs-backpack")

    # ✅ Step 3: Go to cart and start checkout
    cart_page.click_cart_icon()
    cart_page.click_checkout()

    # ✅ Step 4: Fill Checkout Step One (user info)
    checkout_step_one_page.enter_first_name("Tushar")
    checkout_step_one_page.enter_last_name("V")
    checkout_step_one_page.enter_postal_code("110001")
    checkout_step_one_page.click_continue()

    # ✅ Step 5: Checkout Step Two - Finish the purchase
    checkout_step_two_page.click_finish()

    # ✅ Step 6: Verify the confirmation message
    complete_text = checkout_complete_page.get_complete_header_text()
    assert complete_text.strip().lower() == "thank you for your order!".lower()
    print("✅ Order flow completed successfully, confirmation message validated.")

    # ✅ Step 7: Logout from the application
    menu_page.logout()
    print("🔒 Logged out successfully at the end of the test.")