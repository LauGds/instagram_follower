from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = r"D:\Documents\Laura\100_days_coding\chromedriver_win32\chromedriver.exe"
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
SIMILAR_ACCOUNT = "kimkardashian"
SERVICE = Service(CHROME_DRIVER_PATH)


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        email = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(EMAIL)
        time.sleep(1)
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(1)
        log_in = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        log_in.click()
        time.sleep(4)
        notifications_off = self.driver.find_element(by=By.CLASS_NAME, value="_a9_1")
        notifications_off.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/kimkardashian/following/")
        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/'
                                                         'div/div/div/div/div[2]/div/div/div[3]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements(by=By.XPATH, value="//button[contains(.,'Follow')]")
        for button in all_buttons:
            if button.text == 'Follow':
                try:
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(2)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(.,'Following')]")
                    cancel_button.click()


bot = InstaFollower(SERVICE)
bot.login()
bot.find_followers()
bot.follow()
