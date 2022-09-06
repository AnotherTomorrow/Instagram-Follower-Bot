from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaFollwer:
    # -- Initializes driver for self use in class
    def __init__(self, driver):
        self.driver = driver

    # -- Logs into Instagram using credentials stated in main.py
    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        print("Logging onto Instagram")

        sleep(2)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        log_in_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in_btn.click()

    # -- This will go to the instagram page stated in quotations of the search_bar.send_keys attribute and find
    # accounts to follow
    def find_followers(self):
        sleep(4)

        search_bar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys("manga")

        sleep(2)

        first_option = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div['
                                                          '2]/div[3]/div/div[2]/div/div[1]/a')
        first_option.click()

        sleep(2)

        following = self.driver.find_element(By.CSS_SELECTOR, '._aa_h li a')
        href = following.get_attribute("href")
        print(href)

        self.driver.get(href)

        sleep(2)

        scroll = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        # -- Scrolls down by the X amount in the range
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(1)

    # -- Follows all the accounts that have been scrolled through
    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, '._aano div div button')
        # -- loops through each account and follows them with a brief 1-second wait inbetween to diminish the odds of
        # being flagged as a bot or to protect you getting timed out
        for follower in followers:
            follower.click()
            sleep(1)
