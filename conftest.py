# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Chrome options
    options = Options()
    options.headless = False  # <-- ensures the browser is visible
    options.add_argument("--start-maximized")  # optional: start maximized
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Yield driver to tests
    yield driver

    # Cleanup: close browser after tests
    driver.quit()
