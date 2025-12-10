def test_total_consistency(driver):
    driver.get("https://rohcadcurrencycal.netlify.app/")

    driver.find_element("css selector", ".card[data-value='100'] .count").send_keys("1")
    driver.find_element("css selector", ".card[data-value='1'] .count").send_keys("2")

    driver.find_element("id", "calculateBtn").click()

    bills = float(driver.find_element("id", "totalBills").text)
    coins = float(driver.find_element("id", "totalCoins").text)
    grand = float(driver.find_element("id", "grandTotal").text)

    assert grand == bills + coins
