from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from instagram import InstaFollwer

# -- Your credentials here
USERNAME = "Your Username"
PASSWORD = "Your Password"
# -- Your path to Chromedriver.exe here
ser = Service("Your path to Chromedriver.exe")
driver = webdriver.Chrome(service=ser)

follow_bot = InstaFollwer(driver)
follow_bot.login(USERNAME, PASSWORD)
follow_bot.find_followers()
follow_bot.follow()
