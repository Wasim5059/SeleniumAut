import time

import pytest
from selenium import webdriver


def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    # Give some extra argument or extension or anything to Chrome
    # Chrome Options - chrome with the Extension, Window Size, proxy

    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options) #If we open chrome then wont be anything
    driver.get("https://www.google.com/")
    print(driver.title)
    time.sleep(2000)