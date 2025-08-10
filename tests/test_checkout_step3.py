# tests/test_checkout_step3.py

import time
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_complete(setup):
    driver = setup

    # You should already be on checkout step two at this point
    step2 = CheckoutStepTwoPage(driver)
    step2.click_finish()

    complete_page = CheckoutCompletePage(driver)
    
    # Assertions
    assert "checkout-complete.html" in driver.current_url
    assert complete_page.get_thank_you_message() == "Thank you for your order!"
    assert complete_page.is_back_home_button_displayed()
    time.sleep(2)