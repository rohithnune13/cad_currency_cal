def test_empty_calculation(driver):
    driver.get("https://rohcadcurrencycal.netlify.app/")

    driver.find_element("id", "calculateBtn").click()

    assert driver.find_element("id", "totalBills").text == "0.00"
    assert driver.find_element("id", "totalCoins").text == "0.00"
    assert driver.find_element("id", "grandTotal").text == "0.00"
