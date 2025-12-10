def test_page_load(driver):
    driver.get("https://rohcadcurrencycal.netlify.app/")

    assert "Canadian Currency Calculator" in driver.title

    # Check Cashier field
    cashier = driver.find_element("id", "cashier")
    assert cashier.is_displayed()

    # Check calculate button
    calc_btn = driver.find_element("id", "calculateBtn")
    assert calc_btn.is_displayed()

    # Check cards exist
    cards = driver.find_elements("css selector", ".card")
    assert len(cards) >= 10  # Your UI has more but 10 ensures loading
