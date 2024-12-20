import time

import pytest
from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print(driver.title)
    time.sleep(5)
    #driver.close() # it will close the current window and it will not close the other window

    driver.quit() # it will close all the windows
    #Session == None