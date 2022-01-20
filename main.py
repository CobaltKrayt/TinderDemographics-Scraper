from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TinderBot():

    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.wait = WebDriverWait(self.driver, 30)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(1)

        login_btn= self.driver.find_element(By.XPATH,'//*[@id="u-1510067323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

        sleep(1)

        fb_btn = self.driver.find_element(By.XPATH,'//*[@id="u1056518897"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()

        sleep(2)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        sleep(1)

        allow_cookies_btn = self.driver.find_element(By.XPATH,'//button[@data-testid="cookie-policy-dialog-accept-button"]')
        allow_cookies_btn.click()

        email_in = self.driver.find_element(By.XPATH,'//*[@id="email"]')
        email_in.send_keys('danieljames441441@gmail.com')

        pw_in = self.driver.find_element(By.XPATH,'//*[@id="pass"]')
        pw_in.send_keys('Manutd2018')

        login_btn = self.driver.find_element(By.NAME,'login')
        login_btn.click()

        self.driver.switch_to.window(base_window)

        sleep(6)

        popup_1 = self.driver.find_element(By.XPATH,'//button[@data-testid="allow"]')
        popup_1.click()

        sleep(1)

        popup_2 = self.driver.find_element(By.XPATH,'//button[@data-testid="decline"]')
        popup_2.click()

    def swipe_left(self):
        swipe_left_btn = self.driver.find_element(By.XPATH,'//*[@id="Tinder"]/body')
        swipe_left_btn.send_keys(Keys.ARROW_LEFT)

    def open_description(self):
        open_description_btn = self.driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
        open_description_btn.send_keys(Keys.ARROW_UP)

    def grab_info(self):
        info_card = self.driver.find_element(By.XPATH,'//*[@id="u-1510067323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]').text
        print(info_card)

    def auto_swipe(self):
        while True:
            sleep(1)

            try:
                blank_click_btn = self.driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
                blank_click_btn.send_keys(Keys.ESCAPE)
                sleep(1)

            finally:
                self.open_description()
                sleep(0.5)
                self.grab_info()
                sleep(0.5)
                self.swipe_left()




bot = TinderBot()
bot.login()
bot.auto_swipe()
