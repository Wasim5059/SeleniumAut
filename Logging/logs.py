# Logging means - Capture details, which are useful while debugging
# We can show the user details about execution of program
# Warning to the users
#Information to the users
# Errors , Critical Errors user
from selenium import webdriver
import logging

def test_open_login():
    driver = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
    #Create a session with Post Request
    #Fresh Chrome Browser will be open. Session ID is Created. #4w545435
    driver.get("https://www.google.com/")
    driver.maximize_window()
    LOGGER.info(driver.title)
