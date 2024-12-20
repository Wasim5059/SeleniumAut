import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    #return driver also same as yield but return will store permanently but yield is a temporary memory

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    driver.maximize_window()
    #for Verification - we use assert function
    #Actual result == expected result
