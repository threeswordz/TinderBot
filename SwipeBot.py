from selenium import webdriver
from time import sleep

from secrets import username, password

class SwipeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(5)
    
        # login only using fb
        try:
            self.fb_login()
            self.login_to_swipe_menu()
        except IndexError:
            try:
                self.escape_mobile()
                self.fb2_login()
                self.login_to_swipe_menu()
            except Exception:
                pass

        #close all popups before swipe menu
        self.close_popups_before_swipe_menu()

        #auto swipe
        self.auto_swipe()

    def fb_login(self):
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()        

    def escape_mobile(self):
        sleep (5)
        escape_mobile_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button')
        escape_mobile_btn.click()

        toprightlogin_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        toprightlogin_btn.click()

        moreoptions_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button')
        moreoptions_btn.click()

    def fb2_login(self):
        fb2_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button')
        fb2_btn.click()

    def login_to_swipe_menu(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(10)

        self.driver.switch_to.window(base_window)

    def close_popups_before_swipe_menu(self):
        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

        popup_3 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        popup_3.click()

        sleep(2)

        popup_4 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        popup_4.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1.7)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_0 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_0.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = SwipeBot()
bot.login()