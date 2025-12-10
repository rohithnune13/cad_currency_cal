import time

def test_calculation(driver):

    driver.get("https://rohcadcurrencycal.netlify.app/")

    # Select card for $100 bill
    hundred_input = driver.find_element("css selector", ".card[data-value='100'] .count")
    hundred_input.clear()
    hundred_input.send_keys("2")

    # Select card for $20 bill
    twenty_input = driver.find_element("css selector", ".card[data-value='20'] .count")
    twenty_input.clear()
    twenty_input.send_keys("5")

    # Click calculate
    driver.find_element("id", "calculateBtn").click()
    time.sleep(2)

    # Now verify totals
    total_bills = driver.find_element("id", "totalBills").text
    grand_total = driver.find_element("id", "grandTotal").text

    assert total_bills == "300.00"     # (2×100 + 5×20)
    assert grand_total == "300.00"
