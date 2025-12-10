import time

def test_checkout_modal(driver):
    driver.get("https://rohcadcurrencycal.netlify.app/")

    # Fill cashier
    cashier = driver.find_element("id", "cashier")
    cashier.send_keys("Rohith")

    # Set a bill value
    bill_50 = driver.find_element("css selector", ".card[data-value='50'] .count")
    bill_50.clear()
    bill_50.send_keys("2")

    driver.find_element("id", "calculateBtn").click()
    time.sleep(2)

    # Click checkout
    driver.find_element("id", "checkoutBtn").click()
    time.sleep(2)

    # Modal validations
    modal_cashier = driver.find_element("id", "checkoutCashier").text
    assert modal_cashier == "Rohith"

    modal_total = driver.find_element("id", "checkoutTotal").text
    assert modal_total == "100.00"

    # Close modal
    close_btn = driver.find_element("css selector", "#checkoutModal button")
    close_btn.click()
