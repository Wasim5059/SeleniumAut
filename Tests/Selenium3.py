import pytest
from selenium import webdriver

#if we browse the chrome then it will convert into http request (API)
# Then it will hit the selenium server then perform the given code
def test_open_login():
    driver = webdriver.Chrome()
    #Create a session with Post Request
    #Fresh Chrome Browser will be open. Session ID is Created. #4w545435
    driver.get("https://www.google.com/")
    driver.maximize_window()
