from selenium import webdriver
#Create a session
# send the commands - Navigate to a url
#if you are using Selenium  < 4, we use to set the Driver path
#if you are using the Selenium > 4, Driver path is not needed. they will handle automatically
#4.10 
browser = webdriver.Chrome()
browser.get("https://app.vwo.com")

